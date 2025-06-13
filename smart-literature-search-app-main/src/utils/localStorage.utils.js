const setItemWithExpiry = (key, value, timeInMinutes) => {
    const now = new Date();
    const ttlInSeconds = timeInMinutes * 1000 * 60;
    const item = {
      value,
      expiry: now.getTime() + ttlInSeconds,
    };
    localStorage.setItem(key, JSON.stringify(item));
  };
  
  const getItemWithExpiry = (key) => {
    const itemStr = localStorage.getItem(key);
    if (!itemStr) return null;
  
    const item = JSON.parse(itemStr);
    const now = new Date();
    if (now.getTime() > item.expiry) {
      localStorage.removeItem(key);
      return null;
    }
    return item.value;
  };
  
  const deleteItem = (key) => {
    return new Promise((resolve, reject) => {
      localStorage.removeItem(key);
      resolve();
    })
    
  };
  
  const setItem = (key, value) => {
    localStorage.setItem(key, JSON.stringify(value));
  };
  
  const getItem = (key) => {
    return JSON.parse(localStorage.getItem(key));
  };
  
  export default {
    setItemWithExpiry,
    getItemWithExpiry,
    deleteItem,
    setItem,
    getItem,
  };
  