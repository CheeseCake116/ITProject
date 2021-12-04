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
$file = "pixar_comment.out";
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
    $imgSrc="images/pixar_ruka.jpg";
    $movieName="루카";
    $movieSrc="https://www.youtube.com/embed/yCTUWA4G39g";
    $introText="<p><b>바다 밖은 위험해?! 아니, 궁금해!</b><br>
                    이탈리아 리비에라의 아름다운 해변 마을, 바다 밖 세상이 궁금하지만, 두렵기도 한 호기심 많은 소년 '루카'<br>
                    <br>
                    자칭 인간세상 전문가 ‘알베르토’와 함께 모험을 감행하지만, 물만 닿으면 바다 괴물로 변신하는 비밀 때문에 아슬아슬하기만 하다.<br>
                    <br>
                    새로운 친구 ‘줄리아’와 함께 젤라또와 파스타를 실컷 먹고 스쿠터 여행을 꿈꾸는 여름은 그저 즐겁기만 한데…<br>
                    <br>
                    과연 이들은 언제까지 비밀을 감출 수 있을까?<br>
                    <br>
                    함께라서 행복한 여름, 우리들의 잊지 못할 모험이 시작된다!</p>";
} elsif ($index eq "2") {
    $imgSrc="images/pixar_soul.jpg";
    $movieName="소울";
    $movieSrc="https://www.youtube.com/embed/Q0zFPlArth0";
    $introText="<p><b>나는 어떻게 ‘나’로 태어나게 되었을까?<br>
지구에 오기 전 영혼들이 머무는 ‘태어나기 전 세상’이 있다면?</b><br>
뉴욕에서 음악 선생님으로 일하던 ‘조’는<br>
 꿈에 그리던 최고의 밴드와 재즈 클럽에서 연주하게 된 그 날,<br>
 예기치 못한 사고로 영혼이 되어 ‘태어나기 전 세상’에 떨어진다.<br>
 <br>
 탄생 전 영혼들이 멘토와 함께 자신의 관심사를 발견하면 지구 통행증을 발급하는 ‘태어나기 전 세상’<br>
 ‘조’는 그 곳에서 유일하게 지구에 가고 싶어하지 않는 시니컬한 영혼 ‘22’의 멘토가 된다.<br>
 <br>
 링컨, 간디, 테레사 수녀도 멘토되길 포기한 영혼 ‘22’<br>
 꿈의 무대에 서려면 ‘22’의 지구 통행증이 필요한 ‘조’<br>
 그는 다시 지구로 돌아가 꿈의 무대에 설 수 있을까?</p>";
} elsif ($index eq "3") {
    $imgSrc="images/pixar_onward.jpg";
    $movieName="온워드";
    $movieSrc="https://www.youtube.com/embed/7CyeDl6wNok";
    $introText="<p><b>마법이 허락된 단 하루, 지금 만나고 싶은 사람이 있나요?</b><br>
마법이 사라진 세상에 살고 있는 취향과 성격 모두 정반대의 두 형제인<br>
 철든 동생 ‘이안’(톰 홀랜드)과 의욕충만 형 ‘발리’(크리스 프랫).<br>
 <br>
 ‘이안’은 태어나서 얼굴도 본 적 없는 아빠를 그리워하던 중, 서프라이즈 생일 선물로<br>
 아빠의 마법 지팡이를 받게 된다. 그러나 실수로, 아빠의 반쪽만 소환시키는 위기가 발생하는데!!<br>
 <br>
 주어진 시간은 단 하루, 두 형제는 완벽한 모습의 아빠를 찾기 위해 모험을 떠나고<br>
 마법으로 절벽을 건너고, 까마귀 봉우리의 힌트를 따라 관문을 통과하지만<br>
 서로 다른 성격으로 인해, 사사건건 부딪히게 되고, 위험이 발생하는데…<br>
 과연 이들은 무사히 기적을 이룰 수 있을까?<br>
 <br>
 기적을 향한 출발, 지금 당신을 만나러 갑니다.</p>";
} elsif ($index eq "4") {
    $imgSrc="images/pixar_toystory4.jpg";
    $movieName="토이스토리 4";
    $movieSrc="https://www.youtube.com/embed/u8GQibRXVHg";
    $introText="<p><b>우리의 여행은 아직 끝나지 않았다!</b><br>
장난감의 운명을 거부하고 떠난 새 친구 ‘포키’를 찾기 위해 길 위에 나선 ‘우디’는<br>
 우연히 오랜 친구 ‘보핍’을 만나고 그녀를 통해 새로운 세상에 눈을 뜨게 된다.<br>
 한편, ‘버즈’와 친구들은 사라진 ‘우디’와 ‘포키’를 찾아 세상 밖 위험천만한 모험을 떠나게 되는데…</p>";
} elsif ($index eq "5") {
    $imgSrc="images/pixar_incredibles2.jpg";
    $movieName="인크레더블 2";
    $movieSrc="https://www.youtube.com/embed/zON6Mu9_PC0";
    $introText="<p><b>지금까지의 히어로는 잊어라!</b><br>
슈퍼맘 ‘헬렌’이 국민 히어로 ‘일라스티걸’로 활약하며 세상의 주목을 받자<br>
 바쁜 아내의 몫까지 집안일을 하기 위해 육아휴직을 낸 아빠 ‘밥’은<br>
 질풍노도 시기의 딸 ‘바이올렛’, 자기애가 넘치는 아들 ‘대쉬’,<br>
 어마무시한 능력을 시도때도 없이 방출하는 막내 ‘잭잭’까지 전담하며<br>
 전쟁같은 하루하루를 보낸다.<br>
 <br>
 그러던 어느 날,<br>
 각자의 위치에서 바쁜 일상을 보내던 슈퍼파워 가족 앞에 새로운 악당이 나타났다!<br>
 <br>
 다시 한번 세상을 구하기 위해 나선 가족은<br>
 ‘인크레더블’한 능력을 발휘할 수 있을까?</p>";
} elsif ($index eq "6") {
    $imgSrc="images/pixar_coco.jpg";
    $movieName="코코";
    $movieSrc="https://www.youtube.com/embed/LmS5KMJTWlA";
    $introText="<p><b>영원히 기억하고 싶은 황홀한 모험이 시작된다!</b><br>
뮤지션을 꿈꾸는 소년 미구엘은 전설적인 가수 에르네스토의 기타에 손을 댔다 ‘죽은 자들의 세상’에 들어가게 된다.<br>
 그리고 그곳에서 만난 의문의 사나이 헥터와 함께 상상조차 못했던 모험을 시작하게 되는데…<br>
 과연 ‘죽은 자들의 세상’에 숨겨진 비밀은? 그리고 미구엘은 무사히 현실로 돌아올 수 있을까?</p>";
}


print header("Content-type: text/html; charset=utf-8");
print<<EOP;
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
	<meta name="author" content="Team Movies">
	<meta name="description" content="This page shows Disney movies, Pixar moview, and Marvel movies and help you find your favorite movies.">
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
                        document.write('<form style="display: flex;" action="pixar_detail.cgi" method="post">');
                        document.write('<input type=hidden name=index value="$index">');
                        document.write('<input type=hidden name=username value="test" id="post_username">');
                        document.write('<input type=text name=comment style="width: 300px;" placeholder="댓글을 입력해 주세요" class="comment-input"></input>');
                        document.write('<input type=submit value="확인" class="comment-button"></input>');
                        document.write('</form>');
                    } else {
                        document.write('<form style="display: flex;" action="pixar_detail.cgi" method="post">');
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