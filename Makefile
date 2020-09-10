default:
	pdflatex EELS_ML
	pdflatex EELS_ML
	bibtex EELS_ML
	pdflatex EELS_ML

clean:
	rm -rf *~ *.bbl *.out *.pdf *.log *.aux *.blg *.toc EELS_ML.pdf sourceplots/*~ sourceplots/*.pdf
