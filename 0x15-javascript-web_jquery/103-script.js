$(function () {
  // Function to fetch and display translation
  function fetchTranslation () {
    const langCode = $('#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + langCode;

    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  }

  // Click event for button
  $('#btn_translate').on('click', function () {
    fetchTranslation();
  });

  // Keypress event for input field (Enter key detection)
  $('#language_code').on('keypress', function (event) {
    if (event.which === 13) { // Enter key code
      fetchTranslation();
    }
  });
});
