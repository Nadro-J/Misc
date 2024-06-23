
## Simple guide to transferring STINK (HDX -> AH -> GLMR)

#### Hydration -> AssetHub
1. Open [Polkadot.JS](https://polkadot.js.org/apps/?rpc=wss://hydradx.paras.ibp.network#/accounts)
2. Go to Developer -> Extrinsics -> Decode
3. Copy the call data below and paste into hex-encoded call
```
0x8905030800010300a10f043205011f0082fc0a0000010300a10f04320556910200000700e40b54020000000003010200a10f01000c691601793de060491dab143dfae19f5f6413d4ce4c363637e5ceacb2836a4e00
```
![enter image description here](https://i.imgur.com/5ZgbJjT.png)
4. Switch from Decode -> Submission
5. Modify the amount you want to send
![enter image description here](https://i.imgur.com/6aODzN8.png)In the example above, 10000000000 is equal to 1 STINK token.

| INT  | U128 |
|--|--|
| 1 | 10000000000   |
| 10 | 100000000000   |
| 100 | 1000000000000   |
| 1,000 | 10000000000000   |
| 10,000 | 100000000000000   |
| 100,000 | 1000000000000000   |
6. Set AccountId32 (This must be the public key of the address you're sending too)
![enter image description here](https://i.imgur.com/Ezwny4h.png)
7. To get the public key of an address, go to [Subscan Account Format Transform](https://polkadot.subscan.io/tools/format_transform)
8. Paste the address into Input Account
![enter image description here](https://i.imgur.com/f11zvnD.png)![enter image description here](https://i.imgur.com/l72VDFu.png)
9. Once the amount + public key has been defined in the call, hit Submit Transaction

---
---

 #### AssetHub -> Moonbeam
 1. Open [Polkadot.JS](https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Fasset-hub-polkadot-rpc.dwellir.com#/accounts)
2. Go to Developer -> Extrinsics -> Decode
3. Copy the call data below and paste into hex-encoded call
```
0x1f0803010100511f03000103009cc8ecbd7d7a475a835f0956e70eb336a847d7600308000002043205011f00c2d4010000000204320556910200001300902df44057979f0000000000
```
![enter image description here](https://i.imgur.com/d6cHVwx.png)
4. Switch from Decode -> Submission
5. Modify the amount you want to send
![enter image description here](https://i.imgur.com/0rinCY2.png)In the example above, 10000000000 is equal to 1 STINK token.

| INT  | U128 |
|--|--|
| 1 | 10000000000   |
| 10 | 100000000000   |
| 100 | 1000000000000   |
| 1,000 | 10000000000000   |
| 10,000 | 100000000000000   |
| 100,000 | 1000000000000000   |

7.  Set AccountKey20 (Moonbeam EVM address)
![enter image description here](https://i.imgur.com/8Rk9qxa.png)8. Once the amount + public key has been defined in the call, hit Submit Transaction

Source: Information collated from various posts on Twitter
Credits: [Leemo](https://x.com/LeemoXD)
 
