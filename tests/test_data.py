
claim_id_1 = "76919a3572a6dcd30a63bcfb750691ea7b52dec2"

claim_id_2 = "63f2da17b0d90042c559cc73b6b17f853945c43e"

nist256p_private_key = """-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIEPiqIzLqiSc/Tiij30pq0EZ+U0sCEcL0Qf7nY7n1+S2oAoGCCqGSM49
AwEHoUQDQgAEHgR2vmSoZ0jPUurrHeZu7XjMLKs2yQfH3yEgbaWiNMlinFZVEX3k
NPam526UIYPB8N8FwU7nJ43wfYZM44moyA==
-----END EC PRIVATE KEY-----
"""

nist384p_private_key = """-----BEGIN EC PRIVATE KEY-----
MIGkAgEBBDBalPFbjUrughXdUBP9tTzJKxUGNVmQYn4CbrI+TwOyuF7D6giHIqTk
e3RG8ajR0xegBwYFK4EEACKhZANiAAQOLHyqwgNaSu/34tCuP7HLfMhZ42nBpR7Q
qOfIYesuh3ZMdsUmLHTqe4JseHyIlo100beoHyI93ioSFy7+DEJxr0EZSUqlh0me
CALdLe/5dwD7PJfv9gDF1PF8GFwHwdA=
-----END EC PRIVATE KEY-----
"""

secp256k1_private_key = """-----BEGIN EC PRIVATE KEY-----
MHQCAQEEIHX+YRM+CZnwvVcgYTw/gyV5qlW/jdJru3vjpID91NcvoAcGBSuBBAAK
oUQDQgAE98sERXnSkw0fEuk5HMbUrV/TcB1ZFHt6oLiCSyqNyba4yJ3RYcAyMENw
RCmzXNV6Gg65hbDiEMTC+blQJfQMBA==
-----END EC PRIVATE KEY-----
"""

nist256p_cert = {
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3059301306072a8648ce3d020106082a8648ce3d030107034200041e0476be64a86748cf52eaeb1de66eed78cc2cab36c907c7df21206da5a234c9629c5655117de434f6a6e76e942183c1f0df05c14ee7278df07d864ce389a8c8", 
    "keyType": "NIST256p", 
    "version": "_0_0_1"
  }
}

nist384p_cert = {
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3076301006072a8648ce3d020106052b81040022036200040e2c7caac2035a4aeff7e2d0ae3fb1cb7cc859e369c1a51ed0a8e7c861eb2e87764c76c5262c74ea7b826c787c88968d74d1b7a81f223dde2a12172efe0c4271af4119494aa587499e0802dd2deff97700fb3c97eff600c5d4f17c185c07c1d0", 
    "keyType": "NIST384p", 
    "version": "_0_0_1"
  }
}

secp256k1_cert = {
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3056301006072a8648ce3d020106052b8104000a03420004f7cb044579d2930d1f12e9391cc6d4ad5fd3701d59147b7aa0b8824b2a8dc9b6b8c89dd161c0323043704429b35cd57a1a0eb985b0e210c4c2f9b95025f40c04", 
    "keyType": "SECP256k1", 
    "version": "_0_0_1"
  }
}

example_003 = {
  "language": "en", 
  "license": "LBRY Inc", 
  "nsfw": False, 
  "description": "What is LBRY? An introduction with Alex Tabarrok", 
  "content_type": "video/mp4", 
  "author": "Samuel Bryan", 
  "ver": "0.0.3", 
  "title": "What is LBRY?", 
  "sources": {
    "lbry_sd_hash": "d5169241150022f996fa7cd6a9a1c421937276a3275eb912790bd07ba7aec1fac5fd45431d226b8fb402691e79aeb24b"
  }, 
  "thumbnail": "https://s3.amazonaws.com/files.lbry.io/logo.png"
}

example_010 = {
  "version": "_0_0_1", 
  "claimType": "streamType", 
  "stream": {
    "source": {
      "source": "d5169241150022f996fa7cd6a9a1c421937276a3275eb912790bd07ba7aec1fac5fd45431d226b8fb402691e79aeb24b", 
      "version": "_0_0_1", 
      "contentType": "video/mp4", 
      "sourceType": "lbry_sd_hash"
    }, 
    "version": "_0_0_1", 
    "metadata": {
      "license": "LBRY Inc", 
      "description": "What is LBRY? An introduction with Alex Tabarrok", 
      "language": "en", 
      "title": "What is LBRY?", 
      "author": "Samuel Bryan", 
      "version": "_0_1_0", 
      "nsfw": False, 
      "licenseUrl": "", 
      "preview": "", 
      "thumbnail": "https://s3.amazonaws.com/files.lbry.io/logo.png"
    }
  }
}

example_010_serialized = "080110011adc010801129401080410011a0d57686174206973204c4252593f223057686174206973204c4252593f20416e20696e74726f64756374696f6e207769746820416c6578205461626172726f6b2a0c53616d75656c20427279616e32084c42525920496e6338004a2f68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f66696c65732e6c6272792e696f2f6c6f676f2e706e6752005a001a41080110011a30d5169241150022f996fa7cd6a9a1c421937276a3275eb912790bd07ba7aec1fac5fd45431d226b8fb402691e79aeb24b2209766964656f2f6d7034"

claim_010_signed_nist256p = {
  "version": "_0_0_1", 
  "publisherSignature": {
    "certificateId": "63f2da17b0d90042c559cc73b6b17f853945c43e", 
    "signatureType": "NIST256p", 
    "version": "_0_0_1", 
    "signature": "8d555b7db8a9cfbad082b094267304a2cedda61ce3857aeb44f17a9cbc8ee146bab541d2b799992c47a29d34adf588ee0a6becfa10da42d64685a511d7bed45c"
  }, 
  "claimType": "streamType", 
  "stream": {
    "source": {
      "source": "d5169241150022f996fa7cd6a9a1c421937276a3275eb912790bd07ba7aec1fac5fd45431d226b8fb402691e79aeb24b", 
      "version": "_0_0_1", 
      "contentType": "video/mp4", 
      "sourceType": "lbry_sd_hash"
    }, 
    "version": "_0_0_1", 
    "metadata": {
      "license": "LBRY Inc", 
      "description": "What is LBRY? An introduction with Alex Tabarrok", 
      "language": "en", 
      "title": "What is LBRY?", 
      "author": "Samuel Bryan", 
      "version": "_0_1_0", 
      "nsfw": False, 
      "licenseUrl": "", 
      "preview": "", 
      "thumbnail": "https://s3.amazonaws.com/files.lbry.io/logo.png"
    }
  }
}

claim_010_signed_nist384p = {
  "version": "_0_0_1", 
  "publisherSignature": {
    "certificateId": "63f2da17b0d90042c559cc73b6b17f853945c43e", 
    "signatureType": "NIST384p", 
    "version": "_0_0_1", 
    "signature": "6f0fe07f46615d925d018d2e551e0ecb341873c37ffdd5f13909f29b82d36fe02bc9c6e2deea57b1dfa5e6657c31cb46b76028405616149e0c76d0c804e57153b668cd9660bbfed31743fa597f11161a28bba15fa3b0e849b1ffa9ac345eb74b"
  }, 
  "claimType": "streamType", 
  "stream": {
    "source": {
      "source": "d5169241150022f996fa7cd6a9a1c421937276a3275eb912790bd07ba7aec1fac5fd45431d226b8fb402691e79aeb24b", 
      "version": "_0_0_1", 
      "contentType": "video/mp4", 
      "sourceType": "lbry_sd_hash"
    }, 
    "version": "_0_0_1", 
    "metadata": {
      "license": "LBRY Inc", 
      "description": "What is LBRY? An introduction with Alex Tabarrok", 
      "language": "en", 
      "title": "What is LBRY?", 
      "author": "Samuel Bryan", 
      "version": "_0_1_0", 
      "nsfw": False, 
      "licenseUrl": "", 
      "preview": "", 
      "thumbnail": "https://s3.amazonaws.com/files.lbry.io/logo.png"
    }
  }
}

claim_010_signed_secp256k1 = {
  "version": "_0_0_1", 
  "publisherSignature": {
    "certificateId": "63f2da17b0d90042c559cc73b6b17f853945c43e", 
    "signatureType": "SECP256k1", 
    "version": "_0_0_1", 
    "signature": "20b3d8bd3effac3a5121071111d914c48e07bd5ca956b57320f3ffe51dce54b4af522a7bdb295daf3260970d914feb1bb3aa28933949902aa7215427c0a3bac5"
  }, 
  "claimType": "streamType", 
  "stream": {
    "source": {
      "source": "d5169241150022f996fa7cd6a9a1c421937276a3275eb912790bd07ba7aec1fac5fd45431d226b8fb402691e79aeb24b", 
      "version": "_0_0_1", 
      "contentType": "video/mp4", 
      "sourceType": "lbry_sd_hash"
    }, 
    "version": "_0_0_1", 
    "metadata": {
      "license": "LBRY Inc", 
      "description": "What is LBRY? An introduction with Alex Tabarrok", 
      "language": "en", 
      "title": "What is LBRY?", 
      "author": "Samuel Bryan", 
      "version": "_0_1_0", 
      "nsfw": False, 
      "licenseUrl": "", 
      "preview": "", 
      "thumbnail": "https://s3.amazonaws.com/files.lbry.io/logo.png"
    }
  }
}
