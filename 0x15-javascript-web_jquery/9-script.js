$(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr ';

  $.get(url, function (result) {
    $('DIV#hello').text(result.hello);
  });
});
