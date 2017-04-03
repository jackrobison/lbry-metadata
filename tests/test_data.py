

claim_id_1 = "63f2da17b0d90042c559cc73b6b17f853945c43e"

claim_address_2 = "bDtL6qriyimxz71DSYjojTBsm6cpM1bqmj"

claim_address_1 = "bUG7VaMzLEqqyZQAyg9srxQzvf1wwnJ48w"

nist256p_private_key = """-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIGomIxEhgdzuauXte1dEplhvaMNDAATmLVU1jnHjWFtToAoGCCqGSM49
AwEHoUQDQgAEYNJiG34zcuBqhSIdcUiVqZMqneBVw0JuxLzZIHxKXaEtBx0koqB7
rmVwhRspqHv0MZHK8S5N+48RtLuBM2Z8dw==
-----END EC PRIVATE KEY-----
"""

nist384p_private_key = """-----BEGIN EC PRIVATE KEY-----
MIGkAgEBBDDzGJsbIL/j/leqPdsDhco6YxQRA8Dic4zzw5/YWnx66ubbc/dnM9q8
Nq8zCgwGndagBwYFK4EEACKhZANiAAT4Jk/f7PCkodc1cPzBVpA4dzEhamBCQgRs
6RRRRexBIm6kkphyFrWXD7AgSFzsrvtgRFiMZvy8G80QoajN3QnCjbhsJ6bbT3L/
ww5l3R6x6clEQ0yyYmhta1yGqL76r60=
-----END EC PRIVATE KEY-----
"""

secp256k1_private_key = """-----BEGIN EC PRIVATE KEY-----
MHQCAQEEIPZC9hsxKaeG450ATUUZr+LzprYOIznw5ct1FBzDv3choAcGBSuBBAAK
oUQDQgAET2siiLU5trJ6vqyD77ZioqQ8gE7GC8MCDn+Ob3CeANdvT4G2joeTPkEJ
aavGq7zZ++ZsXBIjg//2p1UqXcDQNA==
-----END EC PRIVATE KEY-----
"""

nist256p_cert = {
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3059301306072a8648ce3d020106082a8648ce3d0301070342000460d2621b7e3372e06a85221d714895a9932a9de055c3426ec4bcd9207c4a5da12d071d24a2a07bae6570851b29a87bf43191caf12e4dfb8f11b4bb8133667c77", 
    "keyType": "NIST256p", 
    "version": "_0_0_1"
  }
}

nist384p_cert = {
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3076301006072a8648ce3d020106052b8104002203620004f8264fdfecf0a4a1d73570fcc15690387731216a604242046ce9145145ec41226ea492987216b5970fb020485cecaefb6044588c66fcbc1bcd10a1a8cddd09c28db86c27a6db4f72ffc30e65dd1eb1e9c944434cb262686d6b5c86a8befaafad", 
    "keyType": "NIST384p", 
    "version": "_0_0_1"
  }
}

secp256k1_cert = {
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3056301006072a8648ce3d020106052b8104000a034200044f6b2288b539b6b27abeac83efb662a2a43c804ec60bc3020e7f8e6f709e00d76f4f81b68e87933e410969abc6abbcd9fbe66c5c122383fff6a7552a5dc0d034", 
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
    "signature": "de693b07b28a1981d8c4edec3f8902386953f4fbe8d89ff35037ca22cc9a862793254435d0f2f2d7412378e08a69070597088ffe8a6fd3a85c03e17ec1b9243c"
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
    "signature": "051de53fb07db8b3522f70b586f25379afde28c2e645aab39b3211db034cbabc70dd76ca105f7fcc9e4d8af699250e62412f5b98bd8930ed76eaeacf0465afff605b18cb6379188864a69787de60e456fc283c566d35a5dcdc4cd5c9661c17e7"
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
    "signature": "0def4b70f2af92020b0bd3b8ce73df3067d7b315d40d5c82045af8bc9acf817bb49640a5a6081874d81f2b56065d1065a2bf69471cbb01b4589226179f8b2f41"
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
