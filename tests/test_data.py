
claim_id_1 = "76919a3572a6dcd30a63bcfb750691ea7b52dec2"

claim_id_2 = "63f2da17b0d90042c559cc73b6b17f853945c43e"

nist256p_private_key = """-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIOCaUVbdv50dCmvk3mE0QF6JGmybU45qYVGT6BGAMqCVoAoGCCqGSM49
AwEHoUQDQgAE40/hiuinR9wqJ2w/lBMN48iRSA2McQDJpDUa76M8c5Kif0cJ+Ae5
WIAMH7V/Wr06zxQ0b7Vt+hAFT1KO4KS8Fw==
-----END EC PRIVATE KEY-----
"""

nist384p_private_key = """-----BEGIN EC PRIVATE KEY-----
MIGkAgEBBDCas6kUMXDvqkbS1xlCbAsUWddKmiqXntad2fprJ7jEg4wyh6jUSf6P
AKpz5ghmFQqgBwYFK4EEACKhZANiAATpFanGII5UsTmCwf0jDvl+Rvd3f7w9q9XU
dDyp6Oi1Z57nKXznc7xwZ9Z6uj8GZ6/HC40Z139w2biXPIV++C70WFYjm2Lcb3L+
4iC0ZlG5cbmoKnhKIzXjMdiX6dhMT8s=
-----END EC PRIVATE KEY-----
"""

secp256k1_private_key = """-----BEGIN EC PRIVATE KEY-----
MHQCAQEEIAxnmyRF933DWm/umfiR5y+eV4gw45B2AiRqBv/trQYZoAcGBSuBBAAK
oUQDQgAEt3rQ9pHmyQ+ktObB4mcJmqpr+dw/isX1OBo0HnDjbJFgWIT8ypm1LzfL
CQy/rWs8yYaZcv+ZJIbKg9ti2pmn8Q==
-----END EC PRIVATE KEY-----
"""

nist256p_cert = {
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3059301306072a8648ce3d020106082a8648ce3d03010703420004e34fe18ae8a747dc2a276c3f94130de3c891480d8c7100c9a4351aefa33c7392a27f4709f807b958800c1fb57f5abd3acf14346fb56dfa10054f528ee0a4bc17", 
    "keyType": "NIST256p", 
    "version": "_0_0_1"
  }
}

nist384p_cert = {
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3076301006072a8648ce3d020106052b8104002203620004e915a9c6208e54b13982c1fd230ef97e46f7777fbc3dabd5d4743ca9e8e8b5679ee7297ce773bc7067d67aba3f0667afc70b8d19d77f70d9b8973c857ef82ef45856239b62dc6f72fee220b46651b971b9a82a784a2335e331d897e9d84c4fcb", 
    "keyType": "NIST384p", 
    "version": "_0_0_1"
  }
}

secp256k1_cert = {
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3056301006072a8648ce3d020106052b8104000a03420004b77ad0f691e6c90fa4b4e6c1e267099aaa6bf9dc3f8ac5f5381a341e70e36c91605884fcca99b52f37cb090cbfad6b3cc9869972ff992486ca83db62da99a7f1", 
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
    "signature": "a8ca9aaab647c2e84297726a224d5c8849dc52ecd935160114b7d975c99c113f8f1e0a62e2081af998f9e86bc9c856b0282666b938646a6494417a76947dceed"
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
    "signature": "a0a3d3004be0ca0433309b15ea2ddfee6cd1664b87b53136f0d00a8843c49d6a0caebf18432f7258c44341a4af01c074628c267629523798cf499552d196b10535af3973c506c332bcbb91b634fe5bab1594bb504e5fc8d42405aa848b350e98"
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
    "signature": "af4604eeb8f99da60c2f27c9554ae6164de3e579b6c0f6e2767b5d7c8bc66814fd6d69ebca69dcd30c35b721a6148d04906861412975a712d2ded341c987d70b"
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
