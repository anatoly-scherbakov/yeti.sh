document$.subscribe(function() {
  var tables = document.querySelectorAll("article table:not([data-no-sort])")
  tables.forEach(function(table) {
    new Tablesort(table)
  })
})