// upload_content_save.js

const upload_content_save = document.getElementById('upload_content_save');
upload_content_save.addEventListener('click', () => {
  const input = document.getElementById('upload_file');
  putFile(input.files[0]);
  let file = input.files[0]
})
