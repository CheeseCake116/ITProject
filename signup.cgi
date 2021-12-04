#!/usr/bin/perl -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

$username = param("username");
$userid = param("userid");
$password = param("password");
$passwordCF = param("passwordCF");

$file = "account.out";
open(IN, "$file") || die "can't read the $file";
@lines = <IN>;
close(IN);
$linecnt = @lines;
%account = ();
%names = ();
for ($i=0; $i<$linecnt; $i+=3) {
	$id = @lines[i];
	chomp $id;
	$pwd = @lines[i+1];
	chomp $pwd;
	$name = @lines[i+2];
	chomp $name;
	$account{$id} = $pwd;
	$names{$id} = $name;
}

print header("Content-type: text/html; charset=utf-8");

print<<EOP;
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
	<meta name="author" content="Team Movies">
	<meta name="description" content="This page shows Disney movies, Pixar moview, and Marvel movies and help you find your favorite movies.">
    <title>디즈니 영화</title>
    <link rel="stylesheet" type="text/css" href="css/style.css">
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
</head>
<style>
	section {
		background-image: url(images/signup_image_2.png);
        background-size: auto 100%;
		background-repeat: no-repeat;
        background-position: center;
        width: 100%;
        height: 1200px;
        text-align: center;
    	padding: 150px 0px;
	}
</style>
<body>
    <section>
        <div class="board">

EOP

if (!$username) {
	print "<h3 class='board-text'>이름을 입력해 주세요.</h3>";
	print "<a href='signup.html'><button>돌아가기</button></a>";
} elsif (!$userid) {
	print "<h3 class='board-text'>아이디를 입력해 주세요.</h3>";
	print "<a href='signup.html'><button>돌아가기</button></a>";
} elsif (!$password) {
	print "<h3 class='board-text'>비밀번호를 입력해 주세요.</h3>";
	print "<a href='signup.html'><button>돌아가기</button></a>";
} elsif (!$passwordCF) {
	print "<h3 class='board-text'>비밀번호 확인을 입력해 주세요.</h3>";
	print "<a href='signup.html'><button>돌아가기</button></a>";
} elsif (exists($account{$userid})) {
	print "<h3 class='board-text'>이미 존재하는 아이디입니다.</h3>";
	print "<a href='signup.html'><button>돌아가기</button></a>";
} elsif ($password ne $passwordCF) {
	print "<h3 class='board-text'>비밀번호가 일치하지 않습니다.</h3>";
	print "<a href='signup.html'><button>돌아가기</button></a>";
} else {
	open(OUT, ">>$file") || die "can't write to $file";
	print OUT "$userid\n$password\n$username\n";
	print "<h3 class='board-text'>회원가입을 축하드립니다!.</h3>";
	print "<a href='signin.html'><button>로그인 화면으로</button></a>";
}


print<<EOP;
        </div>
    </section>
</body>
</html>


EOP
