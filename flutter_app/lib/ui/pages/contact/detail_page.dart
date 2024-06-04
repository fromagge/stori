import 'dart:developer';

import 'package:flutter/material.dart';
import 'package:flutter_appo/domain/entities/contact.dart';
import 'package:flutter_appo/provider/contactApi.dart';

class ContactDetailView extends StatefulWidget {
  final Contact contact;

  ContactDetailView({required this.contact});

  @override
  _ContactDetailViewState createState() => _ContactDetailViewState();
}

class _ContactDetailViewState extends State<ContactDetailView> {
  late TextEditingController _firstNameController;
  late TextEditingController _lastNameController;
  late TextEditingController _emailController;
  late TextEditingController _prefixController;
  late TextEditingController _phoneController;

  late TextEditingController _addressController;
  late TextEditingController _cityController;
  late TextEditingController _stateController;
  late TextEditingController _countryController;
  late TextEditingController _zipController;

  @override
  void initState() {
    super.initState();
    _firstNameController =
        TextEditingController(text: widget.contact.firstName);
    _lastNameController = TextEditingController(text: widget.contact.lastName);
    _emailController = TextEditingController(text: widget.contact.email);
    _prefixController =
        TextEditingController(text: widget.contact.prefix.toString());
    _phoneController =
        TextEditingController(text: widget.contact.phone.toString());
    _addressController = TextEditingController(text: widget.contact.address);
    _cityController = TextEditingController(text: widget.contact.city);
    _stateController = TextEditingController(text: widget.contact.state);
    _countryController = TextEditingController(text: widget.contact.country);
    _zipController = TextEditingController(text: widget.contact.zip);
  }

  @override
  void dispose() {
    _firstNameController.dispose();
    _emailController.dispose();
    _prefixController.dispose();
    _phoneController.dispose();
    super.dispose();
  }

  Future<void> _saveContact() async {
    widget.contact.firstName = _firstNameController.text;
    widget.contact.email = _emailController.text;
    widget.contact.prefix = _prefixController.text;
    widget.contact.phone = _phoneController.text;

    try {
      await ContactAPI().updateContact(widget.contact);
      Navigator.pop(context);
    } catch (error) {
      // Handle error
      log('Failed to update contact: $error');
    }
  }

  Future<void> _deleteContact() async {
    try {
      await ContactAPI().deleteContactById(widget.contact.id);
      Navigator.pop(context);
    } catch (error) {
      // Handle error
      log('Failed to delete contact: $error');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Edit'),
        actions: [
          IconButton(
            icon: Icon(Icons.save),
            onPressed: _saveContact,
          ),
          IconButton(
            icon: Icon(Icons.delete),
            onPressed: _deleteContact,
          ),
        ],
      ),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          children: [
            Container(
              margin: EdgeInsets.only(bottom: 20),
              child: TextField(
                controller: _firstNameController,
                decoration: InputDecoration(labelText: 'First Name'),
              ),
            ),
            Container(
              margin: EdgeInsets.only(bottom: 20),
              child: TextField(
                controller: _lastNameController,
                decoration: InputDecoration(labelText: 'Last Name'),
              ),
            ),
            Container(
              margin: EdgeInsets.only(bottom: 20),
              child: TextField(
                controller: _prefixController,
                decoration: InputDecoration(labelText: 'Prefix'),
                keyboardType: TextInputType.number,
              ),
            ),
            Container(
              margin: EdgeInsets.only(bottom: 20),
              child: TextField(
                controller: _phoneController,
                decoration: InputDecoration(labelText: 'Phone number'),
                keyboardType: TextInputType.number,
              ),
            ),
            Container(
              margin: EdgeInsets.only(bottom: 20),
              child: TextField(
                controller: _emailController,
                decoration: InputDecoration(labelText: 'Email'),
              ),
            ),
            Container(
              margin: EdgeInsets.only(bottom: 20),
              child: TextField(
                controller: _addressController,
                decoration: InputDecoration(labelText: 'Address'),
              ),
            ),
            Container(
              margin: EdgeInsets.only(bottom: 20),
              child: TextField(
                controller: _cityController,
                decoration: InputDecoration(labelText: 'City'),
              ),
            ),
            Container(
              margin: EdgeInsets.only(bottom: 20),
              child: TextField(
                controller: _stateController,
                decoration: InputDecoration(labelText: 'State'),
              ),
            ),
            Container(
              margin: EdgeInsets.only(bottom: 20),
              child: TextField(
                controller: _countryController,
                decoration: InputDecoration(labelText: 'Country'),
              ),
            ),
            Container(
              margin: EdgeInsets.only(bottom: 20),
              child: TextField(
                controller: _zipController,
                decoration: InputDecoration(labelText: 'Zip'),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

String? state;
String? country;
String? zip;
