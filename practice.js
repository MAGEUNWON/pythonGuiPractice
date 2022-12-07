function outerFunc(){
  let count = 0;
  function innerFunc(){
    count++;
    console.log(count);
  }
  innerFunc();
  innerFunc();
  innerFunc();
  innerFunc();
}

outerFunc()