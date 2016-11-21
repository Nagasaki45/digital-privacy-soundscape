while inotifywait --quiet --event modify *; do
  make build
done
