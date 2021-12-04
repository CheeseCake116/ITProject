#!/usr/bin/perl -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

$userid = param("userid");
$password = param("password");

$file = "account.out";
open(IN, "$file") || die "can't read the $file";
@lines = <IN>;
close(IN);
$linecnt = @lines;
%account = ();
%names = ();
for ($i=0; $i<$linecnt; $i+=3) {
	$id = $lines[$i];
	chomp $id;
	$pwd = $lines[$i+1];
	chomp $pwd;
	$name = $lines[$i+2];
	chomp $name;
	$account{$id} = $pwd;
	$names{$id} = $name;
}

print header("Content-type: text/html; charset=utf-8");

print<<EOP;
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Disney Movies</title>
    <link rel="stylesheet" type="text/css" href="css/style.css">
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
</head>
<style>
	iframe {
		width: 100%;
	}
</style>
<body>
<div class="container">
    <header>
		<h2><a href="disney.html" target="movieContent">Disney Movies</a></h2>
		<nav>
			<ul>
				<li><a href="disney.html" target="movieContent">Disney</a></li>
				<li><a href="pixar.html" target="movieContent">Pixar</a></li>
				<li><a href="marvel.html" target="movieContent">Marvel</a></li>
				<li><a href="aboutUs.html" target="movieContent">About us</a></li>
			</ul>
		</nav>
		<div class="profile">
        	<img src="images/mypage_1.png" height="40px" style="padding: 0px 20px;">

EOP

if (exists($account{$userid}) && $password eq $account{$userid}) {
	print "<h2 id='username' class='fn-font'>$names{$userid}</h2>";
	print "<a href='index.html' target='_parent' style='margin: auto 0;'><p class='fn-font login-text'>로그아웃</p></a>";
	print "</div>";
	print "</header>";
	print "<iframe name='movieContent' src='disney.html' width='1920px' height='1200px' frameborder='0' scrolling='no'></iframe>";
} elsif (!(exists($account{$userid}))) {
	print "</div>";
	print "</header>";
	print "<iframe name='movieContent' src='signin_iderror.html' width='1920px' height='1200px' frameborder='0' scrolling='no'></iframe>";
} else {
	print "</div>";
	print "</header>";
	print "<iframe name='movieContent' src='signin_pwerror.html' width='1920px' height='1200px' frameborder='0' scrolling='no'></iframe>";
}

print<<EOP;
	
</div>
</body>
</html>

EOP