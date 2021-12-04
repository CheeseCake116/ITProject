#!/usr/bin/perl -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

$index=param("index");
$imgSrc="";
$movieName="";
$movieSrc="";
$introText="";

if ($index eq "1") {
    $imgSrc="images/marvel_eternals.jpg";
    $movieName="이터널스";
    $movieSrc="https://www.youtube.com/embed/BdkSkI61aGo";
    $introText="<p>마블 스튜디오의 <이터널스>는 수 천년에 걸쳐 그 모습을 드러내지 않고 살아온 불멸의 히어로들이<br>
    <어벤져스: 엔드게임> 이후 인류의 가장 오래된 적 '데비안츠'에 맞서기 위해 다시 힘을 합치면서 벌어지는 이야기</p>";
} elsif ($index eq "2") {
    $imgSrc="images/marvel_venom2.jpg";
    $movieName="베놈 2";
    $movieSrc="https://www.youtube.com/embed/BryJA-Xp-Q4";
    $introText="<p><b>히어로의 시대는 끝났다</b><br>
                    ‘베놈’과 완벽한 파트너가 된 ‘에디 브록’(톰 하디) 앞에 ‘클리터스 캐서디’(우디 해럴슨)가 ‘카니지’로 등장,<br>
                    앞으로 닥칠 대혼돈의 세상을 예고한다.<br>
                    대혼돈의 시대가 시작되고, 악을 악으로 처단할 것인가?</p>";
} elsif ($index eq "3") {
    $imgSrc="images/marvel_shangchi.jpg";
    $movieName="샹치와 텐 링즈의 전설";
    $movieSrc="https://www.youtube.com/embed/Pj7CadRf82k";
    $introText="<p><b>'텐 링즈’를 차지하는 자, 세상을 지배한다!</b><br>
초인적인 능력을 가진 ‘텐 링즈’의 힘으로 수세기 동안 어둠의 세상을 지배해 온 ‘웬우’<br>
 '샹치’는 아버지 ‘웬우’ 밑에서 암살자로 훈련을 받았지만 이를 거부하고 평범함 삶을 선택한다.<br>
 그러나 ‘샹치’는 목숨을 노리는 자들의 습격으로 더 이상 운명을 피할 수 없다는 것을 직감하고,<br>
 어머니가 남긴 가족의 비밀과 내면의 신비한 힘을 일깨우게 된다<br>
 벗어나고 싶은 과거이자, 그 누구보다 두려운 아버지 ‘웬우’를 마주해야 하는 ‘샹치’<br>
 악이 될 것인가? 구원이 될 것인가?<br>
 <br>
 마블의 새로운 시대,<br>
 세상에 없던 힘이 탄생한다!</p>";
} elsif ($index eq "4") {
    $imgSrc="images/marvel_blackwidow.jpg";
    $movieName="블랙 위도우";
    $movieSrc="https://www.youtube.com/embed/BOEVQSprNv4";
    $introText="<p><b>'모든 것을 바꾼 그녀의 선택'</b><br>
어벤져스의 운명을 바꾼 블랙 위도우, 그녀의 진짜 이야기가 시작된다!<br>
어벤져스의 히어로 블랙 위도우, ‘나타샤 로마노프’ (스칼렛 요한슨)는<br>
 자신의 과거와 연결된 레드룸의 거대한 음모와 실체를 깨닫게 된다.<br>
 <br>
 상대의 능력을 복제하는 빌런 ‘태스크마스터’와 새로운 위도우들의 위협에 맞서<br>
 목숨을 건 반격을 시작하는 ‘나타샤’는 스파이로 활약했던 자신의 과거 뿐 아니라,<br>
 어벤져스가 되기 전 함께했던 동료들을 마주해야만 하는데…<br>
 <br>
 폭발하는 리얼 액션 카타르시스!<br>
 MCU의 새로운 시대를 시작할 첫 액션 블록버스터를 만끽하라!</p>";
} elsif ($index eq "5") {
    $imgSrc="images/marvel_spiderman3.jpg";
    $movieName="스파이더맨: 파 프롬 홈";
    $movieSrc="https://www.youtube.com/embed/9JtXwsyCqes";
    $introText="<p><b>모든 것이 다시 시작된다!</b><br>
‘엔드게임’ 이후 변화된 세상,<br>
 스파이더맨 ‘피터 파커’는 학교 친구들과 유럽 여행을 떠나게 된다.<br>
 그런 그의 앞에 ‘닉 퓨리’가 등장해 도움을 요청하고<br>
 정체불명의 조력자 ‘미스테리오’까지 합류하게 되면서<br>
 전 세계를 위협하는 새로운 빌런 ‘엘리멘탈 크리쳐스’와<br>
 맞서야만 하는 상황에 놓이게 되는데…</p>";
} elsif ($index eq "6") {
    $imgSrc="images/marvel_xman.jpg";
    $movieName="엑스맨: 다크 피닉스";
    $movieSrc="https://www.youtube.com/embed/PzpZ4aHMXVg";
    $introText="<p><b>두려워하라!<br>
영원한 히어로는 없다</b><br>
어린 시절 비극적 교통사고로 자신의 능력을 알게 된 진 그레이는<br>
 자비에 영재학교에서 새로운 가족을 맞이하게 된다.<br>
 엄청난 잠재적 능력을 지닌 그녀는 엑스맨으로 성장해 우주에서 구조 임무를 수행하던 중<br>
 목숨을 잃을 뻔한 사고를 겪는다. 예기치 못한 사고 이후 폭주하는 힘과<br>
 억눌려왔던 어둠에 눈을 뜨게 된 진 그레이는 엑스맨의 가장 강력하고 파괴적인 적,<br>
 다크 피닉스로 변하게 된다. 프로페서 X는 물론 매그니토까지 능가하는 두려운 존재가 된 그녀 앞에<br>
 힘을 이용하려는 미스터리한 외계 존재가 나타나 그녀를 뒤흔들고,<br>
 지금까지 엑스맨이 이뤄온 모든 것들이 무너지는 가운데<br>
 엑스맨은 사랑하는 친구이자 가장 강력한 적이 된 다크 피닉스와 맞서야 하는데…</p>";
}


print header("Content-type: text/html; charset=utf-8");
print<<EOP;
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="css/style.css">
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
</head>
<body>
	<section>

<div style="background-color: black; width: 100%; height: 600px;">
    <div style="font-size: 1.5em; display: flex; align-items: center; justify-content: space-between;">
        <div style="padding: 30px 100px;">
            <table cellspacing="20">
                <tr>
                    <td>
                        <img src=$imgSrc width="300"/>
                    </td>
                </tr>
                <tr>
                    <th>
                        <p style="font-size: 1.0em;">
                            $movieName
                        </p>
                    </th>
                </tr>
            </table>
        </div>
        <div style="font-size: 1.5em; padding: 30px 20%;">
            <iframe width="640" height="480" src=$movieSrc title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
    </div>
</div>
<article>
    <div style="padding: 50px;">
        <h2>줄거리</h2>
        <br>
        $introText
    </div>
</article>

	</section>
</body>
</html>

EOP