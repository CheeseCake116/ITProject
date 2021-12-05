#!/usr/bin/perl -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

$index=param("index");
$comment=param("comment");
$username=param("username");
$imgSrc="";
$movieName="";
$movieSrc="";
$introText="";
$file = "disney_comment.out";
@comments=();

if ($comment) {
    open(OUT, ">>$file") || die "can't write to the $file";
    print OUT "$index\n$username\n$comment\n";
    close(OUT);
}

open(IN, "$file") || die "can't read the $file";
@comments=<IN>;
close(IN);

$commentCnt = @comments;
$allcomment="";
for ($i=0; $i<$commentCnt; $i+=3) {
	$tempindex = $comments[$i];
	chomp $tempindex;
	$tempusername = $comments[$i+1];
	chomp $tempusername;
	$tempcomment = $comments[$i+2];
	chomp $tempcomment;
    if ($index eq $tempindex) {
        $allcomment = $allcomment."<p style='color: grey;'>작성자 : $tempusername</p>$tempcomment<br><br>";
    }
}

if ($index eq "1") {
    $imgSrc="images/disney_encanto.jpg";
    $movieName="엔칸토";
    $movieSrc="https://www.youtube.com/embed/DJs_ihmMZfg";
    $introText="<p>콜롬비아의 깊은 산 속, 놀라운 마법과 활기찬 매력이 넘치는 세계 ‘엔칸토’. 그 곳에는 특별한 능력을 지닌 마드리갈 패밀리가 살고 있다.<br>
            <br>
            ‘엔칸토’의 마법 덕분에 초인적 힘, 치유하는 힘 등 저마다 특별한 능력을 가지고 태어난 마드리갈 패밀리.<br>
            하지만 ‘미라벨’은 가족 중 유일하게 아무런 능력이 없다.<br>
            <br>
            어느 날, ‘엔칸토’를 둘러싼 마법의 힘이 위험에 처하자 ‘미라벨’은 유일하게 평범한 자신이 특별한 이 가족의 마지막 희망일지 모른다고 생각하는데..<br>
            <br>
            평범한 ‘미라벨’은 과연 기적을 만들 수 있을까?<br>
            <br>
            전 세대 관객들에게 따뜻한 웃음과 감동을 선사할 마법 같은 영화!<br>
            디즈니의 매직이 또 한 번 시작된다</p>";
} elsif ($index eq "2") {
    $imgSrc="images/disney_cruella.jpg";
    $movieName="크루엘라";
    $movieSrc="https://www.youtube.com/embed/yfSMTFzw-Kw";
    $introText="<p>처음부터 난 알았어. 내가 특별하단 걸<br>
 그게 불편한 인간들도 있겠지만 모두의 비위를 맞출 수는 없잖아?<br>
 그러다 보니 결국, 학교를 계속 다닐 수가 없었지<br>
 <br>
 우여곡절 런던에 오게 된 나, 에스텔라는 재스퍼와 호레이스를 운명처럼<br>
 만났고 나의 뛰어난 패션 감각을 이용해 완벽한 변장과 빠른 손놀림으로<br>
 런던 거리를 싹쓸이 했어<br>
 <br>
 도둑질이 지겹게 느껴질 때쯤, 꿈에 그리던 리버티 백화점에 낙하산(?)으로<br>
 들어가게 됐어. 거리를 떠돌았지만 패션을 향한 나의 열정만큼은 언제나<br>
 진심이었거든<br>
 <br>
 근데 이게 뭐야, 옷에는 손도 못 대보고 하루 종일 바닥 청소라니<br>
 인내심에 한계를 느끼고 있을 때, 런던 패션계를 꽉 쥐고 있는 남작 부인이<br>
 나타났어. 천재는 천재를 알아보는 법! 난 남작 부인의 브랜드 디자이너로<br>
 들어가게 되었지<br>
 <br>
 꿈을 이룰 것 같았던 순간도 잠시, 세상에 남작 부인이 ‘그런 사람’이었을<br>
 줄이야…<br>
 <br>
 그래서 난 내가 누군지 보여주기로 했어. 잘가, 에스텔라<br>
 난 이제 크루엘라야!</p>";
} elsif ($index eq "3") {
    $imgSrc="images/disney_raya.jpg";
    $movieName="라야와 마지막 드래곤";
    $movieSrc="https://www.youtube.com/embed/VDgz9xorXE8";
    $introText="<p>인간과 드래곤이 평화롭게 공존하던 신비의 땅, 쿠만드라 왕국<br>
 살아있는 모든 생명을 삼키는 악의 세력 '드룬'이 들이닥치자,<br>
 드래곤들은 인간을 구하기 위해 스스로를 희생하고 전설 속으로 사라진다.<br>
 <br>
 500년 후 부활한 '드룬'이 또다시 세상을 공포에 빠뜨리자,<br>
 전사 ‘라야’는 분열된 쿠만드라를 구하기 위해<br>
 전설 속 마지막 드래곤을 찾아 모험을 떠난다.<br>
 <br>
 그러나, ‘라야’는 험난한 여정을 겪으며 세상을 구하기 위해서는<br>
 전설 속 드래곤보다 더 중요한 것이 있다는 것을 깨닫게 되는데…</p>";
} elsif ($index eq "4") {
    $imgSrc="images/disney_mulan.jpg";
    $movieName="뮬란";
    $movieSrc="https://www.youtube.com/embed/T9ro7JpeoVU";
    $introText="<p>무예에 남다른 재능을 지닌 ‘뮬란’은<br>
 좋은 집안과 인연을 맺어 가문을 빛내길 바라는<br>
 부모님의 뜻에 따라 본연의 모습을 억누르고 성장한다.<br>
 <br>
 어느 날, 북쪽 오랑캐들이 침입하자 황제는 징집령을 내리고<br>
 ‘뮬란’은 아픈 아버지를 대신해 가족들 몰래 전장에 나가기로 결심한다.<br>
 <br>
 여자라는 게 발각되면 목숨을 잃을 수도 있는 상황 속에서<br>
 ‘뮬란’은 타고난 용기와 지혜로 역경을 이겨내며 전사로 성장한다.<br>
 <br>
 마침내 잔인무도한 적장 ‘보리 칸’과 마녀 ‘시아니앙’을 마주하게 된 ‘뮬란’.<br>
 그녀는 위험에 빠진 동료와 가족을 구하고 진정한 전사로 거듭날 수 있을 것인가</p>";
} elsif ($index eq "5") {
    $imgSrc="images/disney_frozen2.jpg";
    $movieName="겨울왕국 2";
    $movieSrc="https://www.youtube.com/embed/eSEs4B4H-EA";
    $introText="<p><b>내 마법의 힘은 어디서 왔을까?<br>
나를 부르는 저 목소리는 누구지?</b><br>
어느 날 부턴가 의문의 목소리가 엘사를 부르고, 평화로운 아렌델 왕국을 위협한다.<br>
 트롤은 모든 것은 과거에서 시작되었음을 알려주며 엘사의 힘의 비밀과 진실을 찾아 떠나야한다고 조언한다.<br>
 <br>
 위험에 빠진 아렌델 왕국을 구해야만 하는 엘사와 안나는 숨겨진 과거의 진실을 찾아<br>
 크리스토프, 올라프 그리고 스벤과 함께 위험천만한 놀라운 모험을 떠나게 된다.<br>
 자신의 힘을 두려워했던 엘사는 이제 이 모험을 헤쳐나가기에 자신의 힘이 충분하다고 믿어야만 하는데…<br>
 <br>
 두려움을 깨고 새로운 운명을 만나다!</p>";
} elsif ($index eq "6") {
    $imgSrc="images/disney_maleficent2.jpg";
    $movieName="말레피센트 2";
    $movieSrc="https://www.youtube.com/embed/sXjwpMDrMnY";
    $introText="<p>동화는 끝났다!<br>
두 세계의 운명을 건 가장 사악한 전쟁이 시작된다!<br>
강력한 어둠의 지배자이자 무어스 숲의 수호자 ‘말레피센트’는 딸처럼 돌봐온 ‘오로라’와 ‘필립 왕자’의 결혼 약속으로 인간 세계의 ‘잉그리스 왕비’와 대립하게 된다.<br>
 이에 요정과 인간의 오랜 연합이 깨지고 숨겨진 요정 종족 다크페이의 리더 ‘코널’까지 등장하면서 두 세계는 피할 수 없는 거대한 전쟁에 휘말리게 되는데…..</p>";
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
        <div style="background-color: black; width: 100%; height: 540px;">
            <table cellspacing="20" style="font-size: 25px; margin: auto;">
                <tr>
                    <td>
                        <img src=$imgSrc width="300"/>
                    </td>
                    <td width="50px"></td>
                    <td rowspan="2">
                        <iframe width="640" height="480" src=$movieSrc title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                    </td>
                </tr>
                <tr>
                    <th>
                        <p style="font-size: 1.0em;">
                            $movieName
                        </p>
                    </th>
                    <td></td>
                    <td></td>
                </tr>
            </table>
        </div>
        <article style="display: flex; width: 1000px; margin: auto; min-height: 700px;">
            <div style="padding: 50px; width:600px;">
                <h2>줄거리</h2>
                <br>
                $introText
            </div>
            <div style="padding-top: 50px; width:400px;">
                <h2>댓글</h2>
                <br>
                <script>
                    var username = window.parent.document.getElementById("username").innerHTML;

                    if (username) {
                        document.write('<form style="display: flex;" action="disney_detail.cgi" method="post">');
                        document.write('<input type=hidden name=index value="$index">');
                        document.write('<input type=hidden name=username value="test" id="post_username">');
                        document.write('<input type=text name=comment style="width: 300px;" placeholder="댓글을 입력해 주세요" class="comment-input"></input>');
                        document.write('<input type=submit value="확인" class="comment-button"></input>');
                        document.write('</form>');
                    } else {
                        document.write('<form style="display: flex;" action="disney_detail.cgi" method="post">');
                        document.write('<input type=hidden name=index value="$index" disabled>');
                        document.write('<input type=hidden name=username value="test" id="post_username" disabled>');
                        document.write('<input type=text name=comment style="width: 300px;" placeholder="로그인이 필요합니다" class="comment-input" disabled></input>');
                        document.write('<input type=submit value="확인" class="comment-button" disabled></input>');
                        document.write('</form>');
                    }
                    
                    var Myelement = document.getElementById("post_username");
                    Myelement.value = username;
                </script>
                <br>
                <div style="overflow:auto; height: 470px; word-break: break-all;">
                    <p>$allcomment</p>
                </div>
            </div>
        </article>
	</section>
</body>
</html>

EOP