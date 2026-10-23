from content import ROOT, load, native_posts, validate
import sys
try:
    errors = validate(load(), native_posts())
except (ValueError, OSError) as exc:
    errors = [str(exc)]
for error in errors:
    print('INVALID:', error, file=sys.stderr)
if errors:
    raise SystemExit(1)
print('OK: content schemas, visibility and relationships validated')
