const compareDates = (d1, d2) => {
  var parts = d1.split('.');
  var d1 = Number(parts[2] + parts[1] + parts[0]);
  parts = d2.split('.');
  var d2 = Number(parts[2] + parts[1] + parts[0]);
  return d1 <= d2;
};

const getToday = () => {
  const now = new Date();
  const year = now.getFullYear()
  const month = fixNumber(now.getMonth()+1);
  const day = fixNumber(now.getDate());

  return `${day}.${month}.${year}`
}

const fixNumber = (day) => {
  return day < 10 ? `0${day}` : day;
}

export default {
  getToday
}

