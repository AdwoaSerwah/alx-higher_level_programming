$(function () {
  // Add item
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  });

  // Remove item
  $('DIV#remove_item').on('click', function () {
    $('UL.my_list li:last-child').remove();
  });

  // Clear list
  $('DIV#clear_list').on('click', function () {
    $('UL.my_list').empty();
  });
});
