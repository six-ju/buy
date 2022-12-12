$(document).ready(function () {
  set_temp();
  show_comment();
});

function save_comment() {
  $.ajax({
    type: "POST",
    url: "/homework",
    data: { sample_give: "데이터전송" },
    success: function (response) {
      alert(response["msg"]);
      window.location.reload();
    },
  });
}
function show_comment() {
  $.ajax({
    type: "GET",
    url: "/homework",
    data: {},
    success: function (response) {
      alert(response["msg"]);
    },
  });
}
