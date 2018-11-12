<!DOCTYPE html>
<html>
<head>
	<title>Verkefni 6</title>
</head>
<body>
	<h2>Nýskráning</h2>
	<form method="post" action="/donyskra" accept-charset="ISO-8859-1">
		<label>
			Notandanafn:
			<br>
			<input type="text" name="user" required>
		</label>
		<br>
		<label>
			Aðgangsorð:
			<br>
			<input type="text" name="pass" required>
		</label>
		<br>
		<label>
			Nafn:
			<br>
			<input type="text" name="nafn">
		</label>
		<br>
		<label>
			<input type="submit" name="nyskraning">
		</label>
	</form>
	<br>
	________________________________________
	<br>
	<form method="post" action="/doinnskra" accept-charset="ISO-8859-1">
		<label>
			Notandanafn:
			<br>
			<input type="text" name="user" required>
		</label>
		<br>
		<label>
			Aðgangsorð:
			<br>
			<input type="text" name="pass" required>
		</label>
		<br>
		<label>
			<input type="submit" name="innskraning">
		</label>
	</form>
</body>
</html>