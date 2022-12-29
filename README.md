# Title: Wiki Project

## General information designed a Wikipedia-like online encyclopedia Wikipedia is a free online encyclopedia that consists of a number of encyclopedia entries on various topics

## Requirements: Encyclopedia entries stored using a lighter-weight human-friendly markup language. Wikipedia happens to use a markup language called Wikitext, but for this project we’ll store encyclopedia entries using a markup language called Markdown.

Python

Django

Visual Studio

markdown2

## Features: Website fulfills the following requirements

## Entry Page: Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, renders a page that displays the contents of that encyclopedia entry.

## Index Page: index.html is written such that, instead of merely listing the names of all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page.

## Search: Allows the user to type a query into the search box in the sidebar to search for an encyclopedia entry.

## New Page: Clicking “Create New Page” in the sidebar takes the user to a page where they can create a new encyclopedia entry.

## Edit Page: On each entry page, the user is able to click a link to be taken to a page where they can edit that entry’s Markdown content in a textarea

## Random Page: Clicking “Random Page” in the sidebar should takes the user to a random encyclopedia entry. Markdown to HTML Conversion: On each entry’s page, any Markdown content in the entry file is converted to HTML before being displayed to the user using the python-markdown2 package
