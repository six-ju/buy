$(document).ready(function () {

});
// now_date = new Date().toLocaleDateString();
// document.write(now_date);

let today = new Date();
let year = today.getFullYear(); // 년도
let month = today.getMonth() + 1;
let date = today.getDate();
let hours = today.getHours(); // 시
let minutes = today.getMinutes();  // 분
let seconds = today.getSeconds();  // 초
console.log(year)
console.log(month)
console.log(date)
now_date = (year+'-'+month+'-'+date+'-'+hours+'-'+minutes+'-'+seconds)
console.log(now_date)
function upload_button() {
    let title = $('#title').val()
    let category = $('#category').val()
    let won = $('#won').val()
    let date = now_date
    let comment = $('#comment').val()



    if ($("#title").val().length == 0) {
            alert("제목은 필수입니다");
            $("#title").focus();
            return false;
        }
    if ($("#category").val().length == 0 ||$("#category").val() == 'none') {
        alert("카테고리 골라주세요");
        $("#category").focus();
        return false;
    }
    if ($("#won").val().length == 0 || $("#won").val() == "0") {
        alert("시작 금액을 정해주세요");
        $("#won").focus();
        return false;
    }
    if ($("#comment").val().length == 0) {
        alert("내용을 써주세요");
        $("#comment").focus();
        return false;
    }

    $.ajax({
        type: 'POST',
        url: '/upload',
        data: {title_give: title,category_give: category,won_give: won,date_give: date, comment_give: comment},
        success: function (response) {
            alert(response['게시됨!'])
            window.location.reload()
        }
    })
}
