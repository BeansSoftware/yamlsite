# coding: utf-8

import os
import yaml
import logging
from jinja2 import Template
from os import listdir
from shutil import copytree, rmtree
import codecs


log = logging.getLogger("build")


def build(config_file):
    config_file = os.path.abspath(config_file)
    with open(config_file) as _config_file:
        config = yaml.load(_config_file)
        os.chdir(os.path.dirname(config_file))
        for page_file in config["app"]["pages"]:
            with open(page_file) as _page_file:
                page = yaml.load(_page_file)
                log.info("Render page %s", page_file)
                render_page(page, config)
        copy_static(config)


def render_page(page, config):
    html = codecs.open(os.path.join(config["app"]["templates"], page["template"]), "r", "utf-8").read()
    template = Template(html)
    page.update(config)
    text = template.render(page)
    log.debug(text)
    if not os.path.exists(config["app"]["out"]):
        os.mkdir(config["app"]["out"])
    with open(os.path.join(config["app"]["out"], page["out"]), 'w') as _out_file:
        _out_file.write(text.encode('utf-8'))


def copy_static(config):
    for f in listdir(config["app"]["static"]):
        log.info("Copy static %s", f)
        if os.path.exists(os.path.join(config["app"]["out"], config["app"]["static_root"], f)):
            rmtree(os.path.join(config["app"]["out"], config["app"]["static_root"], f))

        copytree(os.path.join(config["app"]["static"], f),  os.path.join(config["app"]["out"], config["app"]["static_root"], f))
