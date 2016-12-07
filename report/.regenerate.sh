while inotifywait --quiet --event move_self --event modify report.md ref.bib; do
  make build
done
