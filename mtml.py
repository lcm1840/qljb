import json
import os
from urllib.parse import quote,unquote
import requests,time,datetime

#美团米粒签到和三餐，变量mttoken=xxxx,不要token=,多号&分割

token0 = os.getenv("mttoken")
token1 = token0.split('&')
sjtime = str(round(time.time()*1000))


#'1685204116681'
gg = requests.request("GET",unquote("http%3A%2F%2Fgh.qninq.cn%2Fhttps%3A%2F%2Fraw.githubusercontent.com%2F241793%2Fbucai2%2Fmain%2Fgg",'utf-8'))
print(gg.text)
for b in range(len(token1)):
    token = token1[b]
    #签到
    url0 = "https://wx.waimai.meituan.com/mtandroid_wmgroup/v1/wlwc/signintask/signin?ui=2425758028&region_id=1000431100&region_version=1685183676441"
    #三餐
    url1 = "https://wx.waimai.meituan.com/mtandroid_wmgroup/v1/wlwc/dinnersignin/sign?ui=2425758028&region_id=1000431100&region_version=1685241430077"


    data0 = 'wm_dtype=V2055A&wm_dversion=6.6.3&wm_dplatform=android&wm_uuid=0000000000000435E7EBB5B5D4E35A28BDB8DB9E7A9C3A167570057842939010&wm_visitid=2b2d2d50-9f50-41f6-a266-479c613e0e8b&wm_appversion=9.22.3&wm_logintoken='+token+'&userToken='+token+'&req_time='+sjtime+'&waimai_sign=%2F&userid=2425758028&user_id=2425758028&lch=1001&sessionId=RYY9AA&province=%E9%95%BF%E6%B2%99&nickName=%E9%BB%91%E6%9A%97%E9%9D%A2182&gender=0&country=%E4%B8%AD%E5%9B%BD&city=%E9%95%BF%E6%B2%99&vatarUrl=https%3A%2F%2Fimg.meituan.net%2Favatar%2Fddcd13692022b8d5e31020988b38299514234.jpg&optimusCode=20&riskLevel=71&partner=4&platform=13&uuid=0000000000000435E7EBB5B5D4E35A28BDB8DB9E7A9C3A167570057842939010&open_id=2425758028&rc_app=4&rc_platform=13&host_version=12.9.404&fpApp=0&fpPlatform=4&host_ctype=mtandroid&wm_uuid_source=client&sdkVersion=2.2.3&wxPrint=WX__ver1.2.0_CCCC_fcD9ZMAVg%2BgPZVbBxMC2CpiSZxaxYmT4tj6qknbdw4a%2BOpidKPfLRpF0qAe8i9yvXkU8gn7BKE71hesT9yiZYt2Sw6oDX4h6MHclI4m98EFgVoPB%2BF8uBAv0mUTxxo6JAsk6IWxvjQuPW8Rx2ZpHFP70bqscIa%2BMtLiyke8zmmpya%2BWPE1JcwTHSEERgMBpyc3jhwywHfd1WBVrOfo4JATqzzZs16Yg%2F6H%2BYLAEghjqjFXhR9Rs19A%2FhnN3FLVyk09MVMKY2CpQrVUlrg5tnVKRxfU19XZZxWtctX7v8wEOV8IrANE7TXlAdc%2BZIlVHuf3gkSgAL0zyvG%2Bvhk%2BUKqN6OjjPcYDqs%2Feikl7r%2F%2FQ1YW2enoHD%2FaRMXCF%2FQUuxcbYsxZqosFbVUnoKxPI7POO4NwJ7Jv%2B0hB5%2Bz2oVbsBAut2g86nnkMbPsZEkzjmrQJB%2BB7r8N6rvxij8ygXaOWc1g2HQlfIQYRlcYhfkoqknFM8cCDTO4pAsyrr11zPYiJXGKNZOixnWx9IQf6rQsIu%2BIFr9nBHQuRNuFJPtKBelPd8Ad9m%2B4bdhtkuElZ6cwNud%2BfeP8Y4OItb7MBTNVUNNI3ERx8fCEO%2FoKJe%2BDXDEMasvLkOdwohapA9LW%2FaUgBICbf9FcrfAaj5hiGMmmyiBYBk7CAXfwrg0RHalLgY9lUY2l6mMWjIajBeacjBvmh1UbZpl4yY8Pn7agDqV2rI4cX4a4i2gGJ0A0pb%2BNT%2FDdZKd8IR6jbe2io6oRtHbC2z%2FMdPJ8Nu%2F%2FPXQj0vQ7gxYLGDT7ov6rgxFjQWkDE91uXZQ0vw%2Fe%2BtRelBTLHCmhYSsKTJbmTiUlZaLu%2BhSajAzmNRNKTL%2FGTO8jVEJAkMf%2BB0vqYf5el%2F0789zCXqCbDY8fB0mdpD5ZNgfFe9PfvKndaW3xWU0gY5jLMiJhYNPf5eGCLzpuQfsnq3FJq5A0ohWD2RV%2BL9EyGz1FVcgj8elBoBLaQ5O6u60%2BBsWzCvuDNJzXkuT6c330%2F91fsNDQ%2BFNWkt5JscTX0nZOBse%2BLqkdoC7PPRswDUQ3dL1s0LuyIdx%2BbFIK1jBYJm7R4GYrQOFlzl1uEtGO7dVJnykLc9jfr8UFXmgq3SiqTv8kJg8nm%2FYKWSSqkior5TqLvQnSOLxpeR30MONpSSafTERUVYxBiTnoFsJu96c9w2VIJB7ou79%2BLk2Pn1iau4JkBulz2myPCZUjTlzgUi%2BM1Q6SnbfzSwzCYLFLEyoD2QgMSDuWaSjG1%2FSyjYFrSmJb5zeCVeA34C9wEHD8hYtByOC29%2FzT9tFfBMcxOvsFH5NIOHYJ5KtYqjIOvTRgFBp1pd0WBz4tZsSvbH6onjRJrmhcZR1RBMvzmd0l317ysRBMuSqumcXM%2BU8hX83JVeG8dCUEjyUXXNp6y2E1oXoNw1LG8Xn3cX2hbBvD%2F83cCkpJJiM2p4YkaU8PQOly%2BdozOrR02aQLJagJoUN4ZHWyjkw9iIu17MbWUsCHHcPZBOFrgw0mJvdykviOyuAfQXMypF0Amgu17aI5VXxe6p8fhv0o%2F2DNi1u9GrrO62STUs1wbibdWeLFgrWYfFRA7gw9wA3YJ63hnulY8IZqqhql1OEF5sM2VGRPk8deiWTntK98v2CaTkX3EP6gJ2Z7t0NdZ6%2BMJdV3OaknuU80Z0XC2yuoGGMAajn6mCNOwEgSO8dp2q0gtHWlxALIviFDAgZLJgLVDO89oHtTc6v0%2FnnABf2%2FIkIfLIKVNrUOm0vZPGFCAeZEcKnL%2FULp0DuBMaW6xwutjnxnrwSn2Xa4JBsLguqii4GevfR21foZMF9USRGsshCnGvdfjzRfc5%2FLff5aiXALmmkztFtScivuJBUZw73%2ByOR%2B4eC7PTDTGssK17UdaCYykQitK2yMLuNTLx19LkMCQdYJAIVmgE0lIlyt2%2F1Xi5YasnTtwmWTOJZ5vp53lzY1DzXFUcYk95AAPzeUnI2bqiEIJy7kUNb3ZNwW2LX2JoTqywpxNRzfT2VmBWY%2BWU3I9Nj7cFQQQtKe3FTaAYBkfmSGEBT47J1GycrKHvX%2FhG5S2g4m%2BigHUfKtN0Quna6oh78GHCkx0RG0Ip5WX0h7WOpRZcxrwIM22Jg%2BWpm6X7xkZaYeVeNJiKOsW%2FPA9SrJodTfea4GXjDsd2frOJP%2FOD%2FAfX%2FZDs%2B%2FsbcarAE2xcdgYPmzASKpg7WQ7LTdKprgoZkg4sKJT8ISxYR49Y7j3y7wyh5Ti7oiOEgVgMOhTr57wdf9U4BK8dwdXbQ7gu7SBupFt8LwOLUeUYGK6tnZDo7Geo0d0my5n22LPtQRIAMEQQuR%2FYdMdTv7FMfmUj7WyHPNdYKJEuVCwCEGTKMG6oMWpUrBa4Na%2Bxy8mn1Z4LNoUzdIbchBcZ7sECqRiL1fIgljPeeje2mcGuEDQ7OOWRWu575vMjoZjNgLYB9rUXLl9tELmFvCcJqrGihdVDYgwrgLW%2FDsh9nA5xE2uVdsQcNBTBbsdmeg0lfOFrXH%2Fk8XKrfGtWc3BHycC4ZlSQHfeg9LQell0rs2swnh0Lyn59mn%2B%2BX4wHWknctv76nV%2B4caU38fP%2BOqvo2081bnqC8O2geCD%2FshLcRMWqfysG91qQgd9qEqR1HqCLy76mI7qRpDx81%2BWuqWeg6gpyF%2BRiDdVfNHNmCkfFL4lFr3yZUTNQa02zAnaFlqlmhOdNWxUUq8Edib%2B5WZySLqddNJmn8DLN61JMj%2BsxcMG7ivrDOJ4%2BVW0jGnjZS4x%2Frg1Xy9yulp6uVEuqcknwigTfwVHUjTHj%2BNkvB5BIt4R3qT%2B2kS6Hryspevt947s9YFejZux7g8PstPjqOzIRdlsNiDENYoBG8pO7f3WfEE6Ljf7ArAfdpda4Uku1cxXyVUXGR0D32RDG44gKPlxy5NUG166MUB%2BhoZhOhfvvELS%2BGEo4CWadpMarPweFLwberD4gPgGa95SbV2yE%2F6vETUzxbq5K7HNFRMKefvXHLFAdHEaay4ZdbTXfk4U7TZwPQWQi7RhWGFBGrtFBNaPxMPu6kKGQ7uMawsVP334zuT7DoGXXpDhGH6QRDgCwwszadCn%2BCweNq%2BJCYuAPaNfVKj6ZRydLzE1kJgM6rgfjCp5qQyiOGEWg9NmdZ6ozBPiEvVkADEDqVp0hKIb7PpA%2F4Aamt8C2ecSBve4IFSJCp6uUrELc0MA%2FJt2b2oWd86gXkKfW9Qdip3rqpR%2BT4LWVcdG8b2zrr6xExlOa%2BZPohNTSnr%2BO%2Fwt%2FIzxosKpQyVm%2Fp%2BnM5p2Xz4HZ%2FjO9YfWdV%2F01%2Bz5QlLQB%2FqH3A1llJ9TruaXsqTMtO%2BeVoawJ84Qmz5LHGFLxlCf%2BMSKBAlsgzY2Mn4qMuS8jLgFUpzWlhpuLB%2F0hi8s1D%2FNzZ5rI0fDMNetQ9d5yQm1FSGWUyObIRERsjTnz48VaYqhAwMOEMzyuy564l4eMM%2BneIk%2FmgTQg0eahsjI6FFq9i%2FLSUujjR2M49qZ8qovPV6u4d0h9Xw1Yyloel1&wxNickName=%E9%BB%91%E6%9A%97%E9%9D%A2182&wxAvatar=https%3A%2F%2Fimg.meituan.net%2Favatar%2Fddcd13692022b8d5e31020988b38299514234.jpg&city_id_level2=430100&city_id_level3=430102&actual_city_id_level2=430100&actual_city_id_level3=430102&rank_list_id=134b18045ae336624b867a9c3a167570&wm_ctype=mtandroid_wmgroup'
    data1 = "wm_dtype=V2055A&wm_dversion=6.6.3&wm_dplatform=android&wm_uuid=0000000000000435E7EBB5B5D4E35A28BDB8DB9E7A9C3A167570057842939010&wm_visitid=d42cb97f-ed43-4263-a713-6b07cb99fa34&wm_appversion=9.22.3&wm_logintoken="+token+"&userToken="+token+"&req_time="+sjtime+"&waimai_sign=%2F&userid=2425758028&user_id=2425758028&lch=1001&sessionId=ALXSYU&province=%E9%95%BF%E6%B2%99&nickName=%E9%BB%91%E6%9A%97%E9%9D%A2182&gender=0&country=%E4%B8%AD%E5%9B%BD&city=%E9%95%BF%E6%B2%99&vatarUrl=https%3A%2F%2Fimg.meituan.net%2Favatar%2Fddcd13692022b8d5e31020988b38299514234.jpg&optimusCode=20&riskLevel=71&partner=4&platform=13&uuid=0000000000000435E7EBB5B5D4E35A28BDB8DB9E7A9C3A167570057842939010&open_id=2425758028&rc_app=4&rc_platform=13&host_version=12.9.404&fpApp=0&fpPlatform=4&host_ctype=mtandroid&wm_uuid_source=client&sdkVersion=2.2.3&wxPrint=WX__ver1.2.0_CCCC_fcD9ZMAVg%2BgPZVbBxMC2CpiSZxaxYmT4tj6qknbdw4a%2BOpidKPfLRpF0qAe8i9yvXkU8gn7BKE71hesT9yiZYt2Sw6oDX4h6MHclI4m98EFgVoPB%2BF8uBAv0mUTxxo6JlzI6T1yGK7385OCFqHZDnZeYZC5pk7L6nyhLtG1HXsteavM9qrKI%2BxU3kBiYvvb%2BsOlxG4EaO2xaMnl2LK93PEvQhtaAPVmK%2F2PPqyhr1UAm9Lhm6esPolCikBga%2FCZ%2Fw%2F3aqsZ7L9x%2B%2F020POVcgkR6sPO0iMpNPegvZMAgyAB7EUCCDNnlD7iWxfkBgJGO%2BTt9KQBNDtMkp7vhz2fJjDcT5h42IbFBbBCXhFb8Pj5JH9GATByFy9CGC97V3gslMy7XPBVF16F%2Fpk2xBZHjXu5Q2a%2BJo23yJ%2B36Nt4%2FeHNvsTehcIr%2Frme1VJQqyhPVmSFRZXbsyuoxwSq0MdCljJE785XAbtu9GYZwePeUvl14qger6QdWBCGb06hX1OvoCqYtAG4TlYwX%2B9Li5eRMjp4c5RJzWnEUBEoUWc4N9v95kCWSvj256PLOwri7GqUy3TcEAp4z7dwBKJsmvTKiPzqTYCW5M9FbFF5v3phRuXEG1Ez%2FqeYlor%2BA%2Fh5SrYFKC8%2BbSMuAv32K7CRL2nCIlR%2F87km7mc7N%2B83IpdMcfnu5%2BwqQBy9xPZSI77L8M6Y25pTLzPkoZGDjJSDQtG52PGuliP52NTnsKJzSjOetRSEHrfh56EjD2wi7EJ26AaWkatM3Z%2FeleCk2ax9wGlSisJToWafx9kBxEFB3dQYvNHdmkaQA9eBk758Ql%2F%2BjnhJXbhNt0L07QCVct%2Fz2tlxOObzvEFpW2sDhfU9xyaQpoPoXIzUnvcXpcBD6xPNeCGniMsw0PYal4B3xtcSxJjExyAnnAT0mTmk98Pae3%2F5i7cZ%2FNgFWtFV6qy%2FwbrBvFVeCzD3F1roIwQAA5QfHYLlfC7BVZhnWGkFfWzXlQuT7zEVEuYfIhw5UQodeD2v45dGnmq8FWOdtBn35N%2Fg2Xk12ItqvvY1g0GX9nleXi%2Fju2iSRoybPn%2BxIYvIxj48VPkcEHi8tMht2K5FA7YOfanhX8YhaBwsANlkGv1Lqz7eP%2FW6aemEhG21IJxl4p0Ta66HV77ihjng6hTBKxMuO9LpXC%2BXp20RC%2FbUJ5O57I1ev18Kp0z7yQknkiYP8Yoy7HDBdRyRDVxYw6y9H7OaCYHIQol6ONkNh8CnWfbGkGbsDIE9W68wll5%2FeBFBHomEjIeKuNUiy81h5O%2BDhPVLAn3LaUDdPFfugLtEVVvFoIcvNVVjmZDs5SfwmHzrUKhNUDIkrOJZd%2FGUrbJPeswPVXUyB0DUNLpHTEs5ZE6N2V3AF1GQW9pzZJ%2FjzBouzErlHfXpix3BnH4G8KvF%2FaYBxlYotZ1LQnTatnfAVYmWtbnSC14t3zgS4Mv0CrxLswikkSImxZB08WXGLDirp7132RhaKk0rnPzWvTLtmSBpy0gVNiN1ar%2F%2F13Y4jwYcUOjvIJtueHYKnWrmikMwsX13kXwP3gNwwqK7dwzozf8L8K5uBM8Ms3lByBA4xklchJn3CMgf1roAODT3MPwUwMjqkwe3svZsMoarzXW242CgCZKHbi6Xs5pHKtNLTlW42SUawtVOA9bFhG5xwyP8ixaQjNMBKewGw3VSyiyyumaSK%2B2m6TGAfVmM7UHJVHZV7qVN%2FB6W5DcKNUSrozZLMuZrV7%2BWGnvaMarGc%2BC8n6N0NnPcpJHRgqZs%2BDJ5XnecaeahIfoSoO1rBiINpQjWh7wXFsjBuiBrVC9CGP0dHteGa1Mae%2FMxUML4yxpusL5vJIpKVKRaYmadKJSM%2Bi77hFdNKSC29QZUgrONfJKeUqHvshT48GDJWMVPtGAuk%2BiZeokQA%2F%2BaKnDYUN6ipIXQfnE2erqWPstt5VLzBp%2FzPDiG5mWpjlUoitlUs5S0YpuAKIas%2B5pVlzqybRZl85jDwJTxizEVUP6WBacmtsqQQnwr2xsaI5jFUkIdIjS1eQajllF%2Fsv%2F7KDf3bxykBthGag4cS4fm6tlsl9iipMp%2BaC2gmU7GdsczyyRWGr%2FiahmKEBvT2F7pjsJzvUjK1KIRPv06Yr8y3dzAOlmHGEBFpow0LGZd03tw5IdeWS1GBvCQ9T1h7rzxilu1XuYsIvPAMLmZLGzI4gLag5gLRA21EMAck%2FgfELs%2FcQuTP0UfZLbYddYDKu68hnqTTr2Bot%2FV47dd3xmKlz6ev4CNO%2FPRq9db4WQKegCloVblEjxZ57sN2G8Lm0M3HbXOactogKeRW43WNre%2FYNcxIhOee8oHjqataeVOgveNCkC4M2lMAnkjwMoGVZImRpIf5uFv0n78FDLu8FH5pV5paPqSoegfRc2JIHCxg91HeiEUCJvt1Z3dRwydX6qv5Je2214mtCAPSkwgktjdD37z4gzARyGDX7Q5fWV2G5l1SpVxfOXaiLbUFGTd6Y%2FOhBpU%2BlsVd%2F7nxtDH2EezCQBKMHGUs1Q1%2BFhnqUAO4IEGbzmJfVswctyaiPS9CJ4XwSu8NXrRbJI7L00VXRpQ9VsNwWQBUYZ8jDCwa6At340t%2BRaGQqNwzrmEyGMjD%2FX4gg7A5Z1igy2vLYBph730V0R5El8Eqkkn0U2Xjmo1FOozM3IHLHjDX32Zswv2zkDC1TneorcfdHgQiWCymi6%2F%2BTdhW%2FwXLFcLLnaQwnb2JHwvIMRvc7UqGnlrZzTrM15XeOiDccklUUpinubZV7ATXIny7nHJuNTIUHqJiAxqmpXmwr3%2FnGIsdFLqYgiFHNsOYY6nkxceOb%2FOTJq%2F1X%2FO6fzZCcJRC4TlPwYs2I2%2BJ1Pr67WrKpwXzIBWiCsTn0gO5959cS%2FViDU%2F3%2BhsYBw1PJGCw7vb%2BwWpuIiv%2FzBrCu6Qc1hGCe6OB2yFXHEh5MO2QP8zoRr8z5HebNzmzgXC2Ca3IMtR5n53n5VryrB9Q7MpdE20kwnPDsAD9Zhae%2FyqlB%2BKGjdkGzV9HtptDfjMnxdm5AEYkGqj1FhTVDcZCjcxKb0FR0LLqZY4paCwxsWf%2FEiOGNsH9ljPs4ZAB89bd2aCXNE4Ek%2FRDs86N%2BY%2BtRwfN4Gbu6%2Be8T1qaFHETVHMaElL%2F0uoxyuEIJKi%2FxUwF%2Fs%2Ba8nRl5Xylfsp%2Bqx1jtRcsexDN7OTAhhtdG3npofRfBsdyz1tXtSZwKRqT%2FC2mAwUfLBcSfWPL3Ty5DWJtnkVgVvhEaicPp%2F1u568JYdcIx%2FBqhPHp%2BIrsE%2B86TD6lfuKTAVupbMJwrUUbNsWmWGQv%2BSPAo8LUeIQTryKrEpokusHhPZVr8fqXLr1ozmlPehQpH23wOwF32kRtVD1oxglFgo5ua85ARxYfWXBcfDYHgVzkNa%2F5PIU0aVDITvYL%2FmqsQXJT6u9LQcC02uGJCkTGpgfrLWoQ0IowXVgVtQ3aKwrG%2FAVRdXqAxotoyLaZdL3V5qu9fTH%2Br2hApU5%2F%2BBRMO6cT%2F%2FtS3QIAhLkIGmoc&wxNickName=%E9%BB%91%E6%9A%97%E9%9D%A2182&wxAvatar=https%3A%2F%2Fimg.meituan.net%2Favatar%2Fddcd13692022b8d5e31020988b38299514234.jpg&action_id=3&city_id_level2=430100&city_id_level3=430102&actual_city_id_level2=430100&actual_city_id_level3=430102&rank_list_id=134b1801f53bd469e3f04435e7ebb5b5&wm_ctype=mtandroid_wmgroup"
    headers0 = {
        'Host': 'wx.waimai.meituan.com',
        'Connection': 'keep-alive',
        'Content-Length': '5192',
        'content-type': 'application/x-www-form-urlencoded',
        'R2X-Referer': 'https://servicewechat.com/wx2c348cf579062e56/0/page-frame.html',
        'retrofit_exec_time': sjtime,
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; V2055A Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.74 Mobile Safari/537.36 MicroMessenger/6.5.7  miniprogram MMP/1.24.0.4.335 group/12.9.404',
        'uuid': '0000000000000435E7EBB5B5D4E35A28BDB8DB9E7A9C3A167570057842939010',
        'wm-ctype': 'wxapp',
        'Accept-Encoding': 'gzip, deflate',


    }
    headers1 ={
        'Host': 'wx.waimai.meituan.com',
        'Connection': 'keep-alive',
        'Content-Length': '5204',
        'content-type': 'application/x-www-form-urlencoded',
        'R2X-Referer': 'https://servicewechat.com/wx2c348cf579062e56/0/page-frame.html',
        'retrofit_exec_time': sjtime,
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; V2055A Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.74 Mobile Safari/537.36 MicroMessenger/6.5.7  miniprogram MMP/1.24.0.4.335 group/12.9.404',
        'uuid': '0000000000000435E7EBB5B5D4E35A28BDB8DB9E7A9C3A167570057842939010',
        'wm-ctype': 'wxapp',
        'Accept-Encoding': 'gzip, deflate',

    }



    print("不才提醒您----------"+"账号"+str(b+1)+"美团米粒中心执行----------\n")
    res0 = requests.request("POST",url0,headers = headers0,data=data0)
    qddata = json.loads(res0.text)
    qddata1 = qddata.get("code")
    qddata2 = qddata.get("msg")
    if qddata1 == 0 and qddata2 == '成功':
        print("开始签到："+qddata2)
    elif qddata1 ==1:
        print("开始签到："+qddata2)
    else:
        print(res0.text)
        continue

    res1 = requests.request("POST",url1,headers=headers1,data=data1)
    scdata = json.loads(res1.text)
    scdata1 = scdata.get("code")
    scdata2 = scdata.get("data")
    scdata5 = scdata.get("msg")
    if scdata1 == 0 and scdata5 == "成功":
        if 7<=datetime.datetime.now().hour <=9:
            sctime = "早餐米粒"
        elif 10<=datetime.datetime.now().hour <=14:
            sctime = "午餐米粒"
        elif 16<=datetime.datetime.now().hour <=21:
            sctime = "晚餐米粒"
        scdata3 = scdata2.get("get_points")
        print(sctime,"领取："+str(scdata3))
    elif scdata1 == 5:
        if 7<=datetime.datetime.now().hour <=9:
            sctime = "早餐米粒"
        elif 10<=datetime.datetime.now().hour <=14:
            sctime = "午餐米粒"
        elif 16<=datetime.datetime.now().hour <=21:
            sctime = "晚餐米粒"
        scdata4 = scdata.get("msg")
        print(sctime,scdata4)
    else:
        print(res1.text)
        continue
