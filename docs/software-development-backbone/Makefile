PORT ?= 8767

.PHONY: render serve
render:
	./j

serve: render
	python3 -m http.server $(PORT) --bind 127.0.0.1 --directory slides
