/**
 * This is an autogenerated file created by the Stencil build process.
 * It contains typing information for all components that exist in this project
 * and imports for stencil collections that might be configured in your stencil.config.js file
 */

import '@stencil/core';

declare global {
  namespace JSX {
    interface Element {}
    export interface IntrinsicElements {}
  }
  namespace JSXElements {}

  interface HTMLStencilElement extends HTMLElement {
    componentOnReady(): Promise<this>;
    componentOnReady(done: (ele?: this) => void): void;

    forceUpdate(): void;
  }

  interface HTMLAttributes {}
}





declare global {

  namespace StencilComponents {
    interface EjConversation {

    }
  }

  interface HTMLEjConversationElement extends StencilComponents.EjConversation, HTMLStencilElement {}

  var HTMLEjConversationElement: {
    prototype: HTMLEjConversationElement;
    new (): HTMLEjConversationElement;
  };
  interface HTMLElementTagNameMap {
    'ej-conversation': HTMLEjConversationElement;
  }
  interface ElementTagNameMap {
    'ej-conversation': HTMLEjConversationElement;
  }
  namespace JSX {
    interface IntrinsicElements {
      'ej-conversation': JSXElements.EjConversationAttributes;
    }
  }
  namespace JSXElements {
    export interface EjConversationAttributes extends HTMLAttributes {

    }
  }
}

declare global { namespace JSX { interface StencilJSX {} } }
