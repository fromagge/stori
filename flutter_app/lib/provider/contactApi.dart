import 'dart:convert';
import 'dart:io';
import 'dart:developer';
import 'package:flutter_appo/domain/entities/contact.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:http/http.dart' as http;

import 'package:flutter_appo/provider/authProvider.dart';

final storage = FlutterSecureStorage();

class ContactAPI {
  static String? CONTACT_API_URL = dotenv.env['CONTACT_API_URL'];

  Future<Map<String, String>> getHeaders () async {
    final token = await storage.read(key: "accessToken");

    return {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': 'Bearer $token',
    };
  }

  Future<List<Contact>> fetchContacts(bool? retried) async {
    final url = Uri.parse('$CONTACT_API_URL/contacts');
    final headers = await getHeaders();
    final response = await http.get(url, headers: headers);

    if (response.statusCode == 403) {

      if (retried!) {
        AuthProvider().logout();
      }else{
        return fetchContacts(true);
      }
    }


    if (response.statusCode == 200) {
      List<dynamic> data = json.decode(response.body);
      log(data.toString());
      return data.map((item) => Contact.fromJson(item)).toList();
    }

    throw const HttpException("Something went wrong..sdsdsd.");
  }

  Future<void> createContact(Contact contact) async {
    final response = await http.post(
      Uri.parse('$CONTACT_API_URL/contacts'),
      headers: {
        'Content-Type': 'application/json',
      },
      body: json.encode(contact.toJson()),
    );

    if (response.statusCode != 201) {
      throw Exception('Failed to create contact');
    }
  }

  Future fetchContactById(String id) async {
    final url = Uri.parse('$CONTACT_API_URL/contacts/$id');
    final headers = await getHeaders();
    final response = await http.get(url, headers: headers);

    if (response.statusCode == 403) {
      throw const HttpException("You don't have permission to access this resource");
    }

    if (response.statusCode == 200) {
      return Contact.fromJson(json.decode(response.body));
    }

    Fluttertoast.showToast(msg: "Something went wrong");
    throw const HttpException("Something went wrong...");
  }

  Future updateContact(Contact contact) async {
    final contactId = contact.id;
    final url = Uri.parse('$CONTACT_API_URL/contacts/$contactId');
    final headers = await getHeaders();
    final response = await http.get(url, headers: headers);


    if (response.statusCode != 200) {
      throw Exception('Failed to update contact');
    }

    return true;
  }

  Future<bool> deleteContactById(String id) async {
    final url = Uri.parse('$CONTACT_API_URL/contacts/$id');
    final headers = await getHeaders();
    final response = await http.delete(url, headers: headers);


    if (response.statusCode != 204) {
      throw Exception('Failed to delete contact');
    }

    await fetchContacts(false);

    return true;
  }
}
