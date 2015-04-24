<?php 
// PHP Version

	$post = array('tcIdentity' => TCKIMLIKNO, 'ticketCategory' => '');

    $ch  = curl_init();

    curl_setopt($ch, CURLOPT_URL, 'https://budo.burulas.com.tr/tr/Dynamic/TcRequest');
	curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
    curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13');
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);

    $page = curl_exec($ch);
	
	print_r($page);
	
	?>
