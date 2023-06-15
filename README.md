# 첫 커밋 전 시행착오
이 작업을 처음에는 multiprocessing의 Pool.map을 이용해 병렬 처리를 하려 했다.
하지만, multiprocessing은 자식을 가질 수 없다고 에러가 발생해 Thread로 처리했다.

지금은 Thread.join을 함수 안에다 해줘서 자식이 모두 끝날 때까지 부모가 기다려야 하는데,
이를 Thread를 전부 모아 main 함수에서 start와 join을 해주면 조금 더 빨리 끝나지 않을까 싶다(추측).

# 실행 예시
shell:
```
python3 main.py https://www.naver.com 3
```

result.txt:
```
[https://www.naver.com :: ]
	| https://help.naver.com/support/service/main.help?serviceNo=605&categoryNo=1991
	| https://help.naver.com/support/service/main.help?serviceNo=605&categoryNo=1987
	| https://nid.naver.com/nidlogin.login
	| https://help.naver.com/support/contents/contents.help?serviceNo=605&categoryNo=18215
	| https://help.naver.com/support/alias/search/word/word_16.naver
	| https://help.naver.com/support/alias/search/word/word_29.naver

[https://nid.naver.com/nidlogin.login :: https://www.naver.com]
	| https://www.naver.com
	| http://www.naver.com/rules/privacy.html
	| https://nid.naver.com/user2/api/route?m=routePwInquiry&lang=ko_KR
	| http://www.naver.com/rules/service.html
	| https://help.naver.com/support/service/main.nhn?serviceNo=532
	| https://nid.naver.com/user2/V2Join?m=agree&lang=ko_KR&domain=www.naver.com
	| http://www.naver.com/rules/disclaimer.html
	| https://nid.naver.com/user2/api/route?m=routeIdInquiry&lang=ko_KR
	| https://www.navercorp.com

[https://nid.naver.com/user2/api/route?m=routeIdInquiry&lang=ko_KR :: https://www.naver.com >> https://nid.naver.com/nidlogin.login]
	| https://help.naver.com/support/alias/membership/p.membership/p.membership_26.naver
	| https://www.navercorp.com/

[https://help.naver.com/support/contents/contents.help?serviceNo=605&categoryNo=18215 :: https://www.naver.com]
	| https://policy.naver.com/rules/youthpolicy.html
	| https://www.navercorp.com

[https://nid.naver.com/user2/api/route?m=routePwInquiry&lang=ko_KR :: https://www.naver.com >> https://nid.naver.com/nidlogin.login]
	| https://www.navercorp.com/
	| https://help.naver.com/support/alias/membership/p.membership/p.membership_26.naver

[https://help.naver.com/support/service/main.help?serviceNo=605&categoryNo=1991 :: https://www.naver.com]
	| https://policy.naver.com/rules/youthpolicy.html
	| https://www.navercorp.com

[https://nid.naver.com/user2/V2Join?m=agree&lang=ko_KR&domain=www.naver.com :: https://www.naver.com >> https://nid.naver.com/nidlogin.login]
	| https://policy.naver.com/policy/privacy.html
	| http://policy.naver.com/policy/privacy.html
	| http://policy.naver.com/policy/disclaimer.html
	| https://help.naver.com/support/home.nhn
	| https://inoti.naver.com/inoti/main.nhn
	| https://help.naver.com/support/contents/contents.nhn?serviceNo=532&categoryNo=1441
	| https://policy.naver.com/policy/service.html
	| http://naver.com
	| http://www.naver.com
	| https://help.naver.com/support/contents/contents.nhn?serviceNo=958&categoryNo=3423
	| http://www.naver.com/
	| https://help.naver.com/
	| https://policy.naver.com/policy-mobile/term.html?type=3
	| https://help.naver.com/alias/privacy/privacy_25.naver
	| https://help.naver.com/support/contents/contents.nhn?serviceNo=532&categoryNo=16952

[https://help.naver.com/support/service/main.help?serviceNo=605&categoryNo=1987 :: https://www.naver.com]
	| https://policy.naver.com/rules/youthpolicy.html
	| https://www.navercorp.com

[https://www.naver.com :: https://www.naver.com >> https://nid.naver.com/nidlogin.login]

[https://www.navercorp.com :: https://www.naver.com >> https://nid.naver.com/nidlogin.login]
	| https://snowcorp.com/ko/
	| https://naver.worksmobile.com/
	| https://campaign.naver.com/environment
	| https://www.naverlabs.com/
	| https://clovanote.naver.com/
	| https://1784.navercorp.com
	| https://m.post.naver.com/viewer/postView.naver?volumeNo=32134415&memberNo=30633733
	| https://webtoonscorp.com/
	| https://linepluscorp.com/
	| https://www.naverfincorp.com
	| https://www.navercloudcorp.com/
	| https://naver.worksmobile.com
	| https://recruit.navercorp.com
	| https://whale.naver.com/ko/
	| https://www.navercloudcorp.com
	| https://www.naverlabs.com/nrobot
	| https://navernow.onelink.me/o5cK/6fmlycyl
	| https://www.naver.com/more.html
	| https://campaign.naver.com/smefullcare/online/

[https://help.naver.com/support/alias/search/word/word_29.naver :: https://www.naver.com]
	| https://policy.naver.com/rules/youthpolicy.html
	| https://www.navercorp.com

[https://policy.naver.com/rules/youthpolicy.html :: https://www.naver.com >> https://help.naver.com/support/contents/contents.help?serviceNo=605&categoryNo=18215]
	| http://recruit.navercorp.com/
	| https://www.navercorp.com/nhn/company/proposalGuide.nhn
	| http://www.naver.com/
	| https://help.naver.com/alias/report/Protection_report.naver
	| http://help.naver.com/
	| http://www.navercorp.com/

[https://help.naver.com/support/alias/search/word/word_16.naver :: https://www.naver.com]
	| https://policy.naver.com/rules/youthpolicy.html
	| https://www.navercorp.com

[https://policy.naver.com/rules/youthpolicy.html :: https://www.naver.com >> https://help.naver.com/support/service/main.help?serviceNo=605&categoryNo=1991]
	| http://www.navercorp.com/
	| http://help.naver.com/
	| http://recruit.navercorp.com/
	| http://www.naver.com/
	| https://www.navercorp.com/nhn/company/proposalGuide.nhn
	| https://help.naver.com/alias/report/Protection_report.naver

[https://www.navercorp.com :: https://www.naver.com >> https://help.naver.com/support/contents/contents.help?serviceNo=605&categoryNo=18215]
	| https://www.naverfincorp.com
	| https://recruit.navercorp.com
	| https://www.navercloudcorp.com/
	| https://naver.worksmobile.com
	| https://whale.naver.com/ko/
	| https://www.navercloudcorp.com
	| https://www.naverlabs.com/nrobot
	| https://navernow.onelink.me/o5cK/6fmlycyl
	| https://www.naver.com/more.html
	| https://campaign.naver.com/smefullcare/online/
	| https://snowcorp.com/ko/
	| https://naver.worksmobile.com/
	| https://www.naverlabs.com/
	| https://campaign.naver.com/environment
	| https://1784.navercorp.com
	| https://clovanote.naver.com/
	| https://webtoonscorp.com/
	| https://linepluscorp.com/
	| https://m.post.naver.com/viewer/postView.naver?volumeNo=32134415&memberNo=30633733

[https://policy.naver.com/rules/youthpolicy.html :: https://www.naver.com >> https://help.naver.com/support/service/main.help?serviceNo=605&categoryNo=1987]
	| https://www.navercorp.com/nhn/company/proposalGuide.nhn
	| https://help.naver.com/alias/report/Protection_report.naver
	| http://help.naver.com/
	| http://www.navercorp.com/
	| http://recruit.navercorp.com/
	| http://www.naver.com/

[https://policy.naver.com/rules/youthpolicy.html :: https://www.naver.com >> https://help.naver.com/support/alias/search/word/word_29.naver]
	| http://www.navercorp.com/
	| http://recruit.navercorp.com/
	| http://www.naver.com/
	| https://www.navercorp.com/nhn/company/proposalGuide.nhn
	| https://help.naver.com/alias/report/Protection_report.naver
	| http://help.naver.com/

[https://help.naver.com/support/service/main.nhn?serviceNo=532 :: https://www.naver.com >> https://nid.naver.com/nidlogin.login]
	| https://policy.naver.com/rules/youthpolicy.html

[https://www.navercorp.com :: https://www.naver.com >> https://help.naver.com/support/service/main.help?serviceNo=605&categoryNo=1987]
	| https://www.navercloudcorp.com/
	| https://naver.worksmobile.com
	| https://recruit.navercorp.com
	| https://whale.naver.com/ko/
	| https://www.navercloudcorp.com
	| https://www.naverlabs.com/nrobot
	| https://navernow.onelink.me/o5cK/6fmlycyl
	| https://www.naver.com/more.html
	| https://campaign.naver.com/smefullcare/online/
	| https://snowcorp.com/ko/
	| https://naver.worksmobile.com/
	| https://campaign.naver.com/environment
	| https://www.naverlabs.com/
	| https://clovanote.naver.com/
	| https://1784.navercorp.com
	| https://m.post.naver.com/viewer/postView.naver?volumeNo=32134415&memberNo=30633733
	| https://webtoonscorp.com/
	| https://linepluscorp.com/
	| https://www.naverfincorp.com

[https://www.navercorp.com :: https://www.naver.com >> https://help.naver.com/support/service/main.help?serviceNo=605&categoryNo=1991]
	| https://whale.naver.com/ko/
	| https://www.naverlabs.com/nrobot
	| https://www.navercloudcorp.com
	| https://navernow.onelink.me/o5cK/6fmlycyl
	| https://www.naver.com/more.html
	| https://campaign.naver.com/smefullcare/online/
	| https://snowcorp.com/ko/
	| https://naver.worksmobile.com/
	| https://campaign.naver.com/environment
	| https://www.naverlabs.com/
	| https://clovanote.naver.com/
	| https://1784.navercorp.com
	| https://webtoonscorp.com/
	| https://linepluscorp.com/
	| https://m.post.naver.com/viewer/postView.naver?volumeNo=32134415&memberNo=30633733
	| https://www.naverfincorp.com
	| https://naver.worksmobile.com
	| https://recruit.navercorp.com
	| https://www.navercloudcorp.com/

[https://www.navercorp.com :: https://www.naver.com >> https://help.naver.com/support/alias/search/word/word_29.naver]
	| https://webtoonscorp.com/
	| https://m.post.naver.com/viewer/postView.naver?volumeNo=32134415&memberNo=30633733
	| https://linepluscorp.com/
	| https://www.naverfincorp.com
	| https://www.navercloudcorp.com/
	| https://naver.worksmobile.com
	| https://recruit.navercorp.com
	| https://whale.naver.com/ko/
	| https://www.navercloudcorp.com
	| https://www.naverlabs.com/nrobot
	| https://navernow.onelink.me/o5cK/6fmlycyl
	| https://campaign.naver.com/smefullcare/online/
	| https://www.naver.com/more.html
	| https://snowcorp.com/ko/
	| https://naver.worksmobile.com/
	| https://www.naverlabs.com/
	| https://campaign.naver.com/environment
	| https://clovanote.naver.com/
	| https://1784.navercorp.com

[https://policy.naver.com/rules/youthpolicy.html :: https://www.naver.com >> https://help.naver.com/support/alias/search/word/word_16.naver]
	| http://help.naver.com/
	| http://www.navercorp.com/
	| http://recruit.navercorp.com/
	| http://www.naver.com/
	| https://www.navercorp.com/nhn/company/proposalGuide.nhn
	| https://help.naver.com/alias/report/Protection_report.naver

[https://www.navercorp.com :: https://www.naver.com >> https://help.naver.com/support/alias/search/word/word_16.naver]
	| https://clovanote.naver.com/
	| https://webtoonscorp.com/
	| https://linepluscorp.com/
	| https://m.post.naver.com/viewer/postView.naver?volumeNo=32134415&memberNo=30633733
	| https://www.naverfincorp.com
	| https://recruit.navercorp.com
	| https://www.navercloudcorp.com/
	| https://naver.worksmobile.com
	| https://whale.naver.com/ko/
	| https://www.navercloudcorp.com
	| https://www.naverlabs.com/nrobot
	| https://navernow.onelink.me/o5cK/6fmlycyl
	| https://www.naver.com/more.html
	| https://campaign.naver.com/smefullcare/online/
	| https://snowcorp.com/ko/
	| https://naver.worksmobile.com/
	| https://www.naverlabs.com/
	| https://campaign.naver.com/environment
	| https://1784.navercorp.com
```