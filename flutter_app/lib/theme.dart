import 'package:flutter/material.dart';

final ThemeData customTheme = ThemeData(
    primaryColor: const Color.fromRGBO(0, 58, 64, 1),
    inputDecorationTheme: const InputDecorationTheme(
        labelStyle: TextStyle(
          color: Color.fromRGBO(0, 0, 0, 0.7), // Custom label color
        ),
        enabledBorder: OutlineInputBorder(
          borderSide: BorderSide(
            color: Color.fromRGBO(
                0, 58, 64, 0.2), // Custom border color when focused
            width: 2.0,
          ),
        ),
        focusedBorder: OutlineInputBorder(
          borderSide: BorderSide(
            color: Color.fromRGBO(0, 58, 64, 1),
            width: 1.0,
          ),
        )),
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ButtonStyle(
        textStyle: WidgetStateProperty.all(const TextStyle(
          color: Colors.black,
          fontSize: 16.0,
          fontWeight: FontWeight.bold,
        )),
        backgroundColor: WidgetStateProperty.all(
            const Color.fromRGBO(0, 58, 64, 1)), // Button background color
        foregroundColor:
            WidgetStateProperty.all(Colors.white), // Button text color
        overlayColor: WidgetStateProperty.all(
          const Color.fromRGBO(0, 58, 64, 1),
        ),
        padding: WidgetStateProperty.all(
            const EdgeInsets.symmetric(horizontal: 16.0, vertical: 12.0)),
        shape: WidgetStateProperty.all(RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12.0),
        )),
      ),
    ));
