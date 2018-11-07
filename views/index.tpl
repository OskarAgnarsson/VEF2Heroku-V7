<!DOCTYPE html>
<html>
<head>
	<title>Verkefni 6</title>
</head>
<body>
	<h2>Nýskráning</h2>
	<form method="post" action="/donyskra">
		<label>
			Notandanafn:
			<input type="text" name="user" required>
		</label>
		<br>
		<label>
			Aðgangsorð:
			<input type="text" name="pass" required>
		</label>
		<br>
		<label>
			Nafn:
			<input type="text" name="nafn">
		</label>
		<label>
			<input type="submit" name="nyskraning">
		</label>
	</form>
</body>
</html>