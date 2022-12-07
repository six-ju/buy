// index.js

const button = document.getElementById('button');
button.addEventListener('click', () => {
  const input = document.getElementById('upload_file');
  putFile(input.files[0]);
})