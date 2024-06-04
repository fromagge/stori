class Contact {
  String id;
  String firstName;
  String? lastName;
  String? email;
  String prefix;
  String phone;
  String? address;
  String? city;
  String? state;
  String? country;
  String? zip;

  Contact({
    required this.id,
    required this.firstName,
    required this.email,
    required this.prefix,
    required this.phone,
    this.lastName,
    this.address,
    this.city,
    this.state,
    this.country,
    this.zip,
  });

  Contact.fromJson(Map<String, dynamic> json)
      : id = json['id'].toString(),
        firstName = json['first_name'] ?? "",
        lastName = json['last_name'] ?? "",
        prefix = json['prefix'].toString(),
        phone = json['phone'].toString(),
        email = json['email'] ?? "",
        address = json['address'] ?? "",
        city = json['city'] ?? "",
        state = json['state'] ?? "",
        country = json['country'] ?? "",
        zip = json['zip'] ?? "";

  toJson() {
    return {
      'firstName': firstName,
      'lastName': lastName,
      'email': email,
      'prefix': prefix,
      'phone': phone,
      'address': address,
      'city': city,
      'state': state,
      'country': country,
      'zip': zip
    };
  }
}
