// 페이지 시작은 전체 보기
$(document).ready(function (){
    feed_box()
});

// 전체 카테고리 보기
function feed_box() {
    $.ajax({
        type: 'GET',
        url: '/main/feed',
        date: {},
        success: function (response) {
            $('#all_feed_box').empty()
            let rows = response['feeds']
            for(let i = 0; i < rows.length; i++) {
                let title =rows[i][0]
                let user_id = rows[i][1]
                let date = rows[i][2]
                let category = rows[i][3]
                let content = rows[i][4]
                let price = rows[i][5]

                let temp_html = `<div class="feed_card" style=" cursor: pointer;" onclick="window.open('/modal_html')" target="_blank">
                                    <h2>${title}</h2>
                                    <h5>ID: ${user_id}</h5>
                                    <h6>작성일: ${date}</h6>
                                    <h6>분류: ${category}</h6>
                                    <div class="bodyBox">
                                        <p>${content}
                                        </p>
                                    </div>
                        
                                    <button class="likeBox">
                                        ❤ like
                                    </button>
                        
                                    <button class="commentBox">
                                        댓글
                                    </button>

                                    <div class="price">
                                        현재 입찰가격: ${price}원
                                    </div>
                                </div> </br>`
                $('#all_feed_box').prepend(temp_html)

            }
        }
    });
}
// IT 카테고리 보기
function feed_box_it() {
    $.ajax({
        type: 'GET',
        url: '/main/IT',
        date: {},
        success: function (response) {
            $('#all_feed_box').empty()
            let rows = response['feeds']
            for(let i = 0; i < rows.length; i++) {
                let title =rows[i][0]
                let user_id = rows[i][1]
                let date = rows[i][2]
                let category = rows[i][3]
                let content = rows[i][4]
                let price = rows[i][5]

                let temp_html = `<div class="feed_card" style=" cursor: pointer;" onclick="window.open('/modal_html')" target="_blank">
                                    <h2>${title}</h2>
                                    <h5>ID: ${user_id}</h5>
                                    <h6>작성일: ${date}</h6>
                                    <h6>분류: ${category}</h6>
                                    <div class="bodyBox">
                                        <p>${content}
                                        </p>
                                    </div>
                        
                                    <button class="likeBox">
                                        ❤ like
                                    </button>
                        
                                    <button class="commentBox">
                                        댓글
                                    </button>

                                    <div class="price">
                                        현재 입찰가격: ${price}원
                                    </div>
                                </div> </br>`
                $('#all_feed_box').prepend(temp_html)

            }
        }
    });
}
// electron 카테고리 보기
function feed_box_electron() {
    $.ajax({
        type: 'GET',
        url: '/main/electron',
        date: {},
        success: function (response) {
            $('#all_feed_box').empty()
            let rows = response['feeds']
            for(let i = 0; i < rows.length; i++) {
                let title =rows[i][0]
                let user_id = rows[i][1]
                let date = rows[i][2]
                let category = rows[i][3]
                let content = rows[i][4]
                let price = rows[i][5]

                let temp_html = `<div class="feed_card" style=" cursor: pointer;" onclick="window.open('/modal_html')" target="_blank">
                                    <h2>${title}</h2>
                                    <h5>ID: ${user_id}</h5>
                                    <h6>작성일: ${date}</h6>
                                    <h6>분류: ${category}</h6>
                                    <div class="bodyBox">
                                        <p>${content}
                                        </p>
                                    </div>
                        
                                    <button class="likeBox">
                                        ❤ like
                                    </button>
                        
                                    <button class="commentBox">
                                        댓글
                                    </button>

                                    <div class="price">
                                        현재 입찰가격: ${price}원
                                    </div>
                                </div> </br>`
                $('#all_feed_box').prepend(temp_html)

            }
        }
    });
}
// life 카테고리 보기
function feed_box_life() {
    $.ajax({
        type: 'GET',
        url: '/main/life',
        date: {},
        success: function (response) {
            $('#all_feed_box').empty()
            let rows = response['feeds']
            for(let i = 0; i < rows.length; i++) {
                let title =rows[i][0]
                let user_id = rows[i][1]
                let date = rows[i][2]
                let category = rows[i][3]
                let content = rows[i][4]
                let price = rows[i][5]

                let temp_html = `<div class="feed_card" style=" cursor: pointer;" onclick="location.href='#';">
                                    <h2>${title}</h2>
                                    <h5>ID: ${user_id}</h5>
                                    <h6>작성일: ${date}</h6>
                                    <h6>분류: ${category}</h6>
                                    <div class="bodyBox">
                                        <p>${content}
                                        </p>
                                    </div>
                        
                                    <button class="likeBox">
                                        ❤ like
                                    </button>
                        
                                    <button class="commentBox">
                                        댓글
                                    </button>

                                    <div class="price">
                                        현재 입찰가격: ${price}원
                                    </div>
                                </div> </br>`
                $('#all_feed_box').prepend(temp_html)

            }
        }
    });
}

// 피드 쓰기 POST
function write_feed() {
    $.ajax({
        type: 'POST',
        url: '/#',
        data: {},
        success: function (response) {

        }
    });
}