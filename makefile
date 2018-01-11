# SVG = $(wildcard svg/*.svg)
# PDF = $(SVG:svg/%.svg=pdf/%.pdf)

all: mining-paper.pdf mining-paper.lof
# all: $(PDF) mining-paper.pdf mining-paper.lof

mining-paper.pdf:	mining-paper.lof
		pdflatex -halt-on-error mining-paper.tex && pdflatex -halt-on-error mining-paper.tex && rm -f *.aux *.log *.blg *.toc *.out
# mining-paper.pdf:	mining-paper.lof
# 		bibtex mining-paper && pdflatex -halt-on-error mining-paper.tex && pdflatex -halt-on-error mining-paper.tex && rm -f *.aux *.log *.blg *.toc *.out
mining-paper.lof:	*.tex
		pdflatex -halt-on-error mining-paper.tex
# $(PDF):	pdf/%.pdf: svg/%.svg
# 		inkscape "$<" --export-pdf="$@"
