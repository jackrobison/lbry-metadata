
claim_id_1 = "8e3472bbf59381a8e45df8d26467a2ff08a52ac0d82678383b83f6dd9765a2ab"

claim_id_2 = "9703427964feb8ce8c35cfe1fbf06b4dd114f2be6f7bbfacbf0f9fb92b78fb79"

nist256p_private_key = """-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIBM3iJ+xJLx3RLngcublNSX8lmEJUoIXf3lrZ3ZnClCAoAoGCCqGSM49
AwEHoUQDQgAEj8okJt9D2FvAyKfB6eHi0NWwdYTzoMzUKTFlnPyWub6NR818YyGY
aorKC8VJDX8/yobC8rf5qXEzagdsEwd7KQ==
-----END EC PRIVATE KEY-----
"""

nist384p_private_key = """-----BEGIN EC PRIVATE KEY-----
MIGkAgEBBDBfujG43IPsUiJH6XWIZKMORqc79yvVIsGKzrhRMObpLGGcPfD1B+Fe
GgVsAGEXvpigBwYFK4EEACKhZANiAAS2ZpILzoFA2v/FNTXixRO6FbqkZvJBygSq
xZO/lViWExg9b+o+u+JS1nI8gyAdtHBXPZROkRY5NFavQf27EDrfJrvrKaFHpLA4
Lfe9TRkWLm5EwvQYULzN4fHrs2J9/TU=
-----END EC PRIVATE KEY-----
"""

secp256k1_private_key = """-----BEGIN EC PRIVATE KEY-----
MHQCAQEEIN0q3R2gAZ0NUwwcXO8Nuq4sWyEpOtKq64BJgU8sXqaCoAcGBSuBBAAK
oUQDQgAEFr7zAdzrSYHxNSsMwsamgwpX312kEymOcF+jTVZ3CPIMJWmkAJj5pQOZ
sTxYKkS4IbXTuIq64BoFiJK4JB21yw==
-----END EC PRIVATE KEY-----
"""

nist256p_cert = {
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3059301306072a8648ce3d020106082a8648ce3d030107034200048fca2426df43d85bc0c8a7c1e9e1e2d0d5b07584f3a0ccd42931659cfc96b9be8d47cd7c6321986a8aca0bc5490d7f3fca86c2f2b7f9a971336a076c13077b29", 
    "keyType": "NIST256p", 
    "version": "_0_0_1"
  }
}

nist384p_cert = {
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3076301006072a8648ce3d020106052b8104002203620004b666920bce8140daffc53535e2c513ba15baa466f241ca04aac593bf95589613183d6fea3ebbe252d6723c83201db470573d944e9116393456af41fdbb103adf26bbeb29a147a4b0382df7bd4d19162e6e44c2f41850bccde1f1ebb3627dfd35", 
    "keyType": "NIST384p", 
    "version": "_0_0_1"
  }
}

secp256k1_cert = {
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3056301006072a8648ce3d020106052b8104000a0342000416bef301dceb4981f1352b0cc2c6a6830a57df5da413298e705fa34d567708f20c2569a40098f9a50399b13c582a44b821b5d3b88abae01a058892b8241db5cb", 
    "keyType": "SECP256k1", 
    "version": "_0_0_1"
  }
}

example_003 = {
  "description": "...", 
  "sources": {
    "lbry_sd_hash": "2d1a78159a6da90f704daa96a44fa68e71340da9ab8d17943148819273e23da37e23b6ffe0794448225c199e97a83bf4"
  }, 
  "nsfw": False, 
  "content_type": "fake/type", 
  "fee": {
    "LBC": {
      "amount": 100, 
      "address": "bTjdL9oMjJBU7NuTjZ7C7XDzCqtDYqE7Ly"
    }
  }, 
  "ver": "0.0.3", 
  "license": "Creative Commons Attribution 3.0 United States", 
  "language": "en", 
  "author": "Fake author", 
  "title": "Fake title", 
  "license_url": "https://creativecommons.org/licenses/by/3.0/us/legalcode", 
  "thumbnail": "lbry.io"
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

example_010_serialized = "080110011acf010801128701080410011a0a46616b65207469746c6522032e2e2e2a0b46616b6520617574686f72322e437265617469766520436f6d6d6f6e73204174747269627574696f6e20332e3020556e697465642053746174657338004224080110011a1955a49b1d01c33149f79927de354c849d7bc8f17c19be64ed46250000c8424a076c6272792e696f52005a001a41080110011a302d1a78159a6da90f704daa96a44fa68e71340da9ab8d17943148819273e23da37e23b6ffe0794448225c199e97a83bf4220966616b652f74797065"

claim_010_signed_nist256p = {
  "version": "_0_0_1", 
  "publisherSignature": {
    "signatureType": "NIST256p", 
    "version": "_0_0_1", 
    "signature": "c98defb5cc8cb3c47ebb2ffd684ba38d4317575eb628e0c43a4e680f36bce35309a04366e3bfc5ec86d10b201b1350ee3b61b4bb0a18e58f7783c8ddb184bffc"
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

claim_010_signed_nist384p = {
  "version": "_0_0_1", 
  "publisherSignature": {
    "signatureType": "NIST384p", 
    "version": "_0_0_1", 
    "signature": "dd116311c1bbf84fdb647cff21bda0dd6d8739d5b05d85d778ffddae8603da53d470582bff5165ce4f46306b1e33559fd334091202fdddd8bca0fbf55051fbe8ebea8b10160d596fdf0bb81f17c16a2ea0a008833fa1061f1526bf32938105b7"
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

claim_010_signed_secp256k1 = {
  "version": "_0_0_1", 
  "publisherSignature": {
    "signatureType": "SECP256k1", 
    "version": "_0_0_1", 
    "signature": "b71cb3e3e93aeb51a08947b05bdbe5a1633a2449707f45f2b1de2d8a6da479a93c364a09cd3f4a0425a34764271a15b3fd9a49144c2b3b3db6b86fdb0370bc9b"
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
