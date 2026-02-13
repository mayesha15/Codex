# Challenge solution notes

Decoded `message.wav` as a 2-tone FSK stream (roughly 700 Hz and 940 Hz), grouped bits using long silence gaps as byte separators, inverted bits, then interpreted bytes as Base64.

Recovered Base64:

`MHJtZ2p7VHUxbTFfYjRoX2lzYzVfdm50cn0=`

Decoded text:

`0rmgj{Tu1m1_b4h_isc5_vntr}`

Given the required flag format `0xfun{...}`, the submitted flag is:

`0xfun{Tu1m1_b4h_isc5_vntr}`
