import 'dart:developer';

import 'package:flutter/material.dart';
import 'package:flutter_appo/domain/entities/contact.dart';
import 'package:flutter_appo/provider/contactApi.dart';
import 'package:flutter_appo/ui/pages/contact/create_page.dart';
import 'package:flutter_appo/ui/pages/contact/detail_page.dart';

class ContactListView extends StatefulWidget {
  @override
  _ContactListViewState createState() => _ContactListViewState();
}

class _ContactListViewState extends State<ContactListView> {
  late Future<List<Contact>> _contacts;

  @override
  void initState() {
    super.initState();
    _contacts = ContactAPI().fetchContacts(false);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: null,
        body: FutureBuilder(
            future: _contacts,
            builder: (ctx, snap) {
              if (snap.connectionState == ConnectionState.waiting) {
                return const Center(child: CircularProgressIndicator());
              } else {
                if (snap.error != null) {
                  log(snap.error.toString());
                  return const Center(child: Text('An error occurred!'));
                } else if (!snap.hasData || snap.data!.isEmpty) {
                  return Scaffold(
                      appBar: AppBar(
                        title: Text('Contacts'),
                        actions: <Widget>[
                          IconButton(
                            icon: Icon(Icons.add),
                            onPressed: () {
                              Navigator.push(
                                context,
                                MaterialPageRoute(
                                    builder: (context) => AddContactView()),
                              );
                            },
                          ),
                        ],
                      ),
                      body: Center(child: Text('No contacts found')));
                } else {
                  return Scaffold(
                    appBar: AppBar(
                      title: Text('Contacts'),
                      actions: <Widget>[
                        IconButton(
                          icon: Icon(Icons.add),
                          onPressed: () {
                            // Add your onPressed code here!
                            print('Button Pressed!');
                          },
                        ),
                      ],
                    ),
                    body: ListView.builder(
                      itemCount: snap.data!.length,
                      prototypeItem: const ListTile(
                        title: Text("Mondá"),
                      ),
                      itemBuilder: (context, index) {
                        return Container(
                            padding:
                                EdgeInsetsDirectional.only(start: 20, end: 20),
                            child: ListTile(
                              title: Text(
                                  "${snap.data![index].firstName} ${snap.data![index].lastName}"),
                              subtitle: Text(
                                  "+${snap.data![index].prefix} ${snap.data![index].phone}"),
                              onTap: () {
                                Navigator.push(
                                  context,
                                  MaterialPageRoute(
                                    builder: (context) => ContactDetailView(
                                        contact: snap.data![index]),
                                  ),
                                );
                              },
                            ));
                      },
                    ),
                  );
                }
              }
            }));
  }
}
