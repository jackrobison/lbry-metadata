
claim_id_1 = "20e015ff947ec279a3cf9d5dc330b34f685c3e3cc50952b1e67c68dec6f73481"

claim_id_2 = "c076b418addd40f672b85387f06af681700749f85134df855542f0493c70be78"

nist256p_private_key = """-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIOhqfJ7tYjZ81cBdk9uMDPvWRHz/+GjigOZvY5Ql/wjSoAoGCCqGSM49
AwEHoUQDQgAEL2a9razYoM7gOrlWlngOJcfTlY/kpTPXzUYV3eoqjKzACmspDeXW
g29cXaMYlSx29JzaPfEiDX0AtB6Fy3zzjw==
-----END EC PRIVATE KEY-----
"""

nist384p_private_key = """-----BEGIN EC PRIVATE KEY-----
MIGkAgEBBDAhce3/LMmFinDapmD0LnWQU1q0l+wyiglQTRH1uRmGA3wDO0hIAQ5f
J2/lAhoCP82gBwYFK4EEACKhZANiAATJ9hE7pCSTF8QJ/oaUWTdablr+u25lwHNu
xrlEgaN3ssgiqR+7yBQTDiiN7tncAnislHxkfL5D/2N7GKFcONwcmhvRCz60MFi2
ApHYzLEgzkHZ+gYxYBmfPFSgVUyVyhU=
-----END EC PRIVATE KEY-----
"""

secp256k1_private_key = """-----BEGIN EC PRIVATE KEY-----
MHQCAQEEIM4LTCu62zb9+VZRvD4FiKhOrtrybd0GaYnsiEifeTyjoAcGBSuBBAAK
oUQDQgAETGShz0zs9khcyX0uwAReQo9ZSS0JUim772ZOaEoRASiwtDPDAwvn46sh
KCXpbE9zwpFdMk61W/4tulQzvvjrjQ==
-----END EC PRIVATE KEY-----
"""

nist256p_cert = {
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3059301306072a8648ce3d020106082a8648ce3d030107034200042f66bdadacd8a0cee03ab95696780e25c7d3958fe4a533d7cd4615ddea2a8cacc00a6b290de5d6836f5c5da318952c76f49cda3df1220d7d00b41e85cb7cf38f", 
    "keyType": "NIST256p", 
    "version": "_0_0_1"
  }
}

nist384p_cert = {
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3076301006072a8648ce3d020106052b8104002203620004c9f6113ba4249317c409fe869459375a6e5afebb6e65c0736ec6b94481a377b2c822a91fbbc814130e288deed9dc0278ac947c647cbe43ff637b18a15c38dc1c9a1bd10b3eb43058b60291d8ccb120ce41d9fa063160199f3c54a0554c95ca15", 
    "keyType": "NIST384p", 
    "version": "_0_0_1"
  }
}

secp256k1_cert = {
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3056301006072a8648ce3d020106052b8104000a034200044c64a1cf4cecf6485cc97d2ec0045e428f59492d095229bbef664e684a110128b0b433c3030be7e3ab212825e96c4f73c2915d324eb55bfe2dba5433bef8eb8d", 
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

claim_010_signed_nist256p = {
  "version": "_0_0_1", 
  "publisherSignature": {
    "signatureType": "NIST256p", 
    "version": "_0_0_1", 
    "signature": "71c4a4a73b91e1d2c2add4e2a7b72e3bde5a1428bb14fdf2de3dc8705ea1e6408b59bd0fbf912702c325ef5777487236cccea48b27ba97951e3a0495b4afd7fb"
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
    "signature": "03ec92cbe95210f01606afe5baa9d78abe8cbabfa9560e3a24770cc7ff6fa8a1fbe3d7270cfcdcfbd425b96d713caeb07e598d68b1ea059aad1d4eb3068d6dc08f6f173f9565408e7c813f46c7bef96b82f37ed51c0d6c1691d4bf87bbcca465"
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
    "signature": "d4fb7b9dbb7024d9f05bc86952f0165f0aa45cbd32d78d734e475f959b39c659ec6fc87494b6c6044b0ee5f20a811a5ab34270b4f64d10287d08eacde81ec7f5"
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
