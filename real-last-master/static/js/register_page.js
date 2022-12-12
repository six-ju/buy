// // Get the modal
// var modal = document.getElementById('id01');
//
// // When the user clicks anywhere outside of the modal, close it
// window.onclick = function(event) {
//     if (event.target === modal) {
//         modal.style.display = "none";
//     }
// }

function duplication() {
    let dp_cn = document.getElementById('dp').value;

    $.ajax({
        type: 'GET',
        url: '/register_page.html/register/duplicate',
        date: {},
        success: function (response) {
            let d = response['dpc']
            for (let i = 0; i < d.length; i++) {
                if (d[i]['user_id'] === dp_cn) {
                    return alert('이미 등록된 아이디입니다.');
                }
            }
            if (dp_cn === '') {
                return alert('아이디를 입력해주세요.')
            }
            for (let i = 0; i < d.length; i++) {
                if (d[i]['user_id'] !== dp_cn && dp_cn !== '') {
                    console.log('true')
                    return alert('사용할 수 있는 아이디입니다.')
                }
            }
        }
    });

}