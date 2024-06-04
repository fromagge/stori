import 'dart:convert';
import 'dart:developer';
import 'dart:io';

import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

final storage = FlutterSecureStorage();

class AuthProvider with ChangeNotifier {
  static final AuthProvider _instance = AuthProvider._internal();
  factory AuthProvider() => _instance;
  AuthProvider._internal();

  bool _isAuthenticated = true;

  bool get isAuthenticated => _isAuthenticated;

  Future<void> login(String username, String password) async {
    await dotenv.load(fileName: ".env");

    final AUTH_API_URL = dotenv.env['AUTH_API_URL'];
    final url = Uri.parse('$AUTH_API_URL/auth/login');

    final body = jsonEncode({
      'username': username,
      'password': password,
    });

    try {
      final response = await http.post(
        url,
        headers: {'Content-Type': 'application/json; charset=UTF-8'},
        body: body,
      );
      log(response.body);

      if (response.statusCode != 200) {
        throw const HttpException("The username or password are incorrect");
      }

      final data = jsonDecode(response.body);

      await Future.wait([
        storage.write(key: 'accessToken', value: data['token']),
        storage.write(key: 'refreshToken', value: data['refresh_token']),
      ]);

      _isAuthenticated = true;
      notifyListeners();
    } on SocketException {
      Fluttertoast.showToast(msg: "You don't have an internet connection");
    } on HttpException {
      Fluttertoast.showToast(msg: "The username or password are incorrect");
    } on Exception catch (e) {
      log(e.toString());
      Fluttertoast.showToast(msg: "Something went wrong");
    }
  }

  void logout() {
    _isAuthenticated = false;
    Fluttertoast.showToast(msg: "Your session has expired");
    notifyListeners();
  }

  void refreshToken() async {
    final AUTH_API_URL = dotenv.env['AUTH_API_URL'];
    final url = Uri.parse('$AUTH_API_URL/auth/refresh_token');

    final refreshToken = await storage.read(key: "refresh_token");

  }
}
