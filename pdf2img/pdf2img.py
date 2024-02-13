"""
Este script converte um arquivo PDF em imagens PNG e salva as imagens no diretório especificado.

Usage:
    python script.py <pdf_path> [-o OUTPUT_FOLDER]

Arguments:
    pdf_path (str): Caminho para o arquivo PDF a ser convertido em imagens PNG.

Options:
    -o OUTPUT_FOLDER, --output_folder OUTPUT_FOLDER: Caminho para a pasta de saída onde as imagens PNG serão salvas (padrão: 'output').

Exemplos de uso:
    # Converter um arquivo PDF 'documento.pdf' em imagens PNG e salvar as imagens em 'output/'
    python script.py documento.pdf

    # Converter um arquivo PDF 'documento.pdf' em imagens PNG e salvar as imagens em 'imagens/'
    python script.py documento.pdf -o imagens/
"""

import argparse
from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path, output_folder):
    """
    Converte um arquivo PDF em imagens PNG e salva as imagens no diretório especificado.

    Args:
        pdf_path (str): Caminho para o arquivo PDF a ser convertido em imagens PNG.
        output_folder (str): Caminho para a pasta de saída onde as imagens PNG serão salvas.

    Returns:
        None

    Raises:
        FileNotFoundError: Se o arquivo PDF especificado não for encontrado.
        Exception: Se ocorrer um erro ao processar o PDF.

    """
    try:
        # Verificar se o diretório de saída existe, se não, criá-lo
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # Converter PDF em imagens PNG
        images = convert_from_path(pdf_path)
        
        # Salvar as imagens no diretório de saída
        for i, image in enumerate(images):
            image_path = os.path.join(output_folder, f"page_{i+1}.png")
            image.save(image_path, "PNG")
            print(f"Imagem salva em: {image_path}")

    except FileNotFoundError:
        print(f"Arquivo '{pdf_path}' não encontrado.")
    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")

if __name__ == "__main__":
    # Configura o parser de argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Convert PDF to PNG images")
    parser.add_argument("pdf_path", help="caminho para o arquivo PDF")
    parser.add_argument("-o", "--output_folder", default="output", help="caminho para a pasta de saída (default: output)")

    # Analisa os argumentos da linha de comando
    args = parser.parse_args()

    # Chama a função para converter o PDF em imagens
    pdf_to_images(args.pdf_path, args.output_folder)
