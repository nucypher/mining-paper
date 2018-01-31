# SVG = $(wildcard svg/*.svg)
# PDF = $(SVG:svg/%.svg=pdf/%.pdf)

all: mining-paper.pdf mining-paper.lof
# all: $(PDF) mining-paper.pdf mining-paper.lof

mining-paper.pdf:	mining-paper.lof
		xelatex -halt-on-error mining-paper.tex && xelatex -halt-on-error mining-paper.tex && rm -f *.aux *.log *.blg *.toc *.out
# mining-paper.pdf:	mining-paper.lof
# 		bibtex mining-paper && xelatex -halt-on-error mining-paper.tex && xelatex -halt-on-error mining-paper.tex && rm -f *.aux *.log *.blg *.toc *.out
mining-paper.lof:	*.tex
		xelatex -halt-on-error mining-paper.tex
# $(PDF):	pdf/%.pdf: svg/%.svg
# 		inkscape "$<" --export-pdf="$@"
