export const create = (tagName, className, content) => {
    const element = document.createElement(tagName);
    className && (element.className = className);
    content && (element.innerHTML = content);
    return element;
};
export const toggleInput = (terminal, enable = false) => {
    // Has to be done in order to preserve the focus on terminal click when disabled
    terminal.input.readOnly = !enable;
    terminal.inputContainer.style.opacity = enable ? '' : '0';
};
