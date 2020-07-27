const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;

document.cookie = "timezone=" + timezone;

console.log(timezone);