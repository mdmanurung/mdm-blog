document.querySelectorAll('[data-catalog]').forEach(catalog => {
  const rows = [...catalog.querySelectorAll('[data-record]')];
  const controls = [...catalog.querySelectorAll('[data-filter]')];
  const apply = () => {
    let count = 0;
    rows.forEach(row => {
      const visible = controls.every(control => {
        const value = control.value.toLocaleLowerCase().trim();
        if (!value) return true;
        if (control.dataset.filter === 'query') return row.textContent.toLocaleLowerCase().includes(value);
        return (row.dataset[control.dataset.filter] || '').split('|').includes(value);
      });
      row.hidden = !visible;
      count += visible ? 1 : 0;
    });
    catalog.querySelector('[data-count]').textContent = `${count} ${count === 1 ? 'result' : 'results'}`;
    catalog.querySelector('[data-empty]').hidden = count !== 0;
  };
  controls.forEach(control => control.addEventListener(control.tagName === 'SELECT' ? 'change' : 'input', apply));
  apply();
});
