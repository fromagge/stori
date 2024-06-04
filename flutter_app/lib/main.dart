import 'dart:developer';

import 'package:flutter/material.dart';
import 'package:flutter_appo/theme.dart';
import 'package:flutter_appo/ui/pages/auth/login.dart';
import 'package:flutter_appo/ui/pages/contact/list_page.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:provider/provider.dart';

import 'package:flutter_appo/provider/authProvider.dart';

Future main() async {
   await dotenv.load(fileName: ".env");

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => AuthProvider(),
      child: MaterialApp(
        title: 'Contact List',
        theme: customTheme,
        home: ContactApp(),
      ),
    );
  }
}

class ContactApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    var authProvider = Provider.of<AuthProvider>(context);

    return authProvider.isAuthenticated ? ContactListView(): LoginPage();
  }
}
