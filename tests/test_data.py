test_ec_priv_key = \
"""-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIA0pP1+zwmzDiImsh6i0z21CB4rjbKD9tejhc1v/61jYoAoGCCqGSM49
AwEHoUQDQgAE71RLHfb3dtV3tYP7fRmmHKqYBpstNbthEjV6XFvyV+zZrUKwUEr3
I8l/VpxKQIrFYstOcRuRAOwTqLVeaDW/nQ==
-----END EC PRIVATE KEY-----"""


fake_stream_claim_id = "aa04a949348f9f094d503e5816f0cfb57ee68a22f6d08d149217d071243e0378"
fake_cert_claim_id = "26ccfc3c4b21d1a6d07e6ff674e5038d3c290df974f3a2a4cb721996f7c882ba"

example_003 = {
    'author': 'Fake author',
    'content_type': 'fake/type',
    'description': '...',
    'language': 'en',
    'license': 'Creative Commons Attribution 3.0 United States',
    'license_url': 'https://creativecommons.org/licenses/by/3.0/us/legalcode',
    'nsfw': False,
    'sources': {
        'lbry_sd_hash': '2d1a78159a6da90f704daa96a44fa68e71340da9ab8d17943148819273e23da37e23b6ffe0794448225c199e97a83bf4',
    },
    'fee': {
        'LBC': {
            'amount': 100,
            'address': 'bTjdL9oMjJBU7NuTjZ7C7XDzCqtDYqE7Ly'
        }
    },
    'thumbnail': 'lbry.io',
    'title': 'Fake title',
    'ver': '0.0.3'
}

example_010 = {
  "version": "_0_0_1",
  "claimType": "streamType",
  "stream": {
    "source": {
      "source": "2d1a78159a6da90f704daa96a44fa68e71340da9ab8d17943148819273e23da37e23b6ffe0794448225c199e97a83bf4",
      "version": "_0_0_1",
      "contentType": "fake/type",
      "sourceType": "lbry_sd_hash"
    },
    "version": "_0_0_1",
    "metadata": {
      "license": "Creative Commons Attribution 3.0 United States",
      "fee": {
        "currency": "LBC",
        "amount": 100.0,
        "version": "_0_0_1",
        "address": "bTjdL9oMjJBU7NuTjZ7C7XDzCqtDYqE7Ly"
      },
      "description": "...",
      "language": "en",
      "title": "Fake title",
      "author": "Fake author",
      "version": "_0_1_0",
      "nsfw": False,
      "licenseUrl": "",
      "preview": "",
      "thumbnail": "lbry.io"
    }
  }
}

example_010_signed = {
  "version": "_0_0_1",
  "publisherSignature": {
    "signatureType": "ECDSA",
    "version": "_0_0_1",
    "signature": "5c722667b8520e4a1263480f0cb43f6b421c8fdb6364b83ac03adb563fe828078555361ff60caa366bec2e9d5de6730aac950b15c0bf4a627de89ac282ef8114"
  },
  "claimType": "streamType",
  "stream": {
    "source": {
      "source": "2d1a78159a6da90f704daa96a44fa68e71340da9ab8d17943148819273e23da37e23b6ffe0794448225c199e97a83bf4",
      "version": "_0_0_1",
      "contentType": "fake/type",
      "sourceType": "lbry_sd_hash"
    },
    "version": "_0_0_1",
    "metadata": {
      "license": "Creative Commons Attribution 3.0 United States",
      "fee": {
        "currency": "LBC",
        "amount": 100.0,
        "version": "_0_0_1",
        "address": "bTjdL9oMjJBU7NuTjZ7C7XDzCqtDYqE7Ly"
      },
      "description": "...",
      "language": "en",
      "title": "Fake title",
      "author": "Fake author",
      "version": "_0_1_0",
      "nsfw": False,
      "licenseUrl": "",
      "preview": "",
      "thumbnail": "lbry.io"
    }
  }
}

example_010_ecdsa_cert = {
  "version": "_0_0_1",
  "claimType": "certificateType",
  "certificate": {
    "publicKey": "3059301306072a8648ce3d020106082a8648ce3d03010703420004ef544b1df6f776d577b583fb7d19a61caa98069b2d35bb6112357a5c5bf257ecd9ad42b0504af723c97f569c4a408ac562cb4e711b9100ec13a8b55e6835bf9d",
    "keyType": "ECDSA",
    "version": "_0_0_1"
  }
}
