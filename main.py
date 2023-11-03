from textwrap import dedent

import streamlit as st


def set_page_configs(icon: str, title: str):
    st.set_page_config(
        page_title=title,
        page_icon=icon,
    )
    st.write(f"## {icon}{title}")
    st.sidebar.header(title)


def display_contents():
    markdown_contents = dedent(
        """
        ### List
        - content1
        - content2
        - content3

        ### Code
        - python
        ```python
        print("hello world")
        ```

        - html
        ```html
        <h1>Title</h1>
        <p>this is sample.</p>
        ```

        ### LaTex
        The below equation represents the motion equation.

        $$
        F = ma
        $$

        here, $F$ is force, $m$ is mass, $a$ is accelaration.
        """
    )
    st.markdown(markdown_contents)


set_page_configs(icon="🐌", title="Streamlit Sample")
display_contents()