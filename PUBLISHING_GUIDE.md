# Publishing Guide for Children's Books via Amazon KDP

This document provides the technical specifications and integration notes for formatting and publishing the generated children's books through Amazon Kindle Direct Publishing (KDP).

---

## 1. Print-Friendly Book Formatting

This section outlines the layout and structure for the final, print-ready PDF that will be uploaded to Amazon.

### 1.1. Page Order & Layout

The book should be structured as follows:

*   **Page 1: Inside Cover / Title Page:**
    *   Content: Book Title, Author's Name (or a placeholder for the user's name).
    *   Layout: Centered text. Illustration can be a small, simple version of the main character.
*   **Page 2-9: Story Pages (8 pages):**
    *   Content: Each page contains one segment of the story and one full-page illustration.
    *   Layout: Text can be overlaid on the illustration in a clear, readable font, or placed in a designated text box at the bottom or top of the page. Ensure high contrast between text and background.
*   **Page 10: "The End" Page:**
    *   Content: A simple "The End" message with a final, small illustration (e.g., the main character waving goodbye).
*   **Page 11: Coloring Pages Title Page:**
    *   Content: "Time to Color!" or a similar fun title.
*   **Page 12-19: Coloring Pages (8 pages):**
    *   Content: The 8 line-art images corresponding to the story illustrations.
*   **Page 20: Blank Page:**
    *   A blank page to ensure the final page count is a multiple of 4, which is often recommended for printing.
*   **Back Cover:** (This is designed separately, see Cover Formatting)

### 1.2. Page Numbering

*   Page numbers should be included, starting from the first story page.
*   They should be small, centered at the bottom of the page, and in a non-intrusive font.
*   The front matter (Title Page) and back matter (Coloring Pages) should not have visible page numbers.

---

## 2. Amazon KDP Specifications

These are the recommended settings for publishing a square children's book.

*   **Ink and Paper Type:** `Premium color ink and 60-71 pound (88-105 GSM) white paper`. This provides the best quality for illustrations.
*   **Trim Size:** `8.5" x 8.5" (21.59 x 21.59 cm)`. This is a popular and well-supported square format for children's books. The minimum page count for this size is 24, but our ~20 pages of content plus front/back matter will fit well within KDP's structure which adds its own pages.
*   **Bleed:** `Bleed` setting should be selected. This means illustrations should extend to the very edge of the page, beyond the trim line, to avoid white borders after printing. The final PDF manuscript should be sized slightly larger (e.g., 8.625" x 8.75") to account for this.
*   **Cover Finish:** `Glossy`. This finish makes colors pop and is durable for children's books.

---

## 3. Online Ordering System Integration (Placeholders)

This section outlines the necessary components for an online ordering system that connects to a print-on-demand service like KDP or another provider (e.g., Lulu).

### 3.1. User Input Fields

The UI must capture the following information:

*   **Recipient's Name:** `[user_name]`
*   **Shipping Address:**
    *   Street Address 1: `[user_address_1]`
    *   Street Address 2 (Optional): `[user_address_2]`
    *   City: `[user_city]`
    *   State/Province: `[user_state]`
    *   Postal Code: `[user_zip]`
    *   Country: `[user_country]`
*   **Custom Dedication (Optional):** A text field for a short, personalized message to be printed on the title page. `[user_dedication]`

### 3.2. Payment Placeholders & API Integration

*   **Payment Gateway:** Integration with a payment processor like Stripe or PayPal is required.
    *   `// Placeholder for Stripe API call`
    *   `// function processPayment(paymentToken, orderDetails) { ... }`
*   **Order Submission:** After successful payment, the system must programmatically submit the order to the printing service.
    *   `// Placeholder for Amazon KDP API call or other print-on-demand service`
    *   `// function submitPrintOrder(orderDetails, pdf_url) { ... }`
    *   **NOTE:** Amazon does not have a simple, direct "print-on-demand" API for individual orders in this manner. This typically requires a more complex setup, potentially involving manual order placement or using a third-party service that *does* have a print API and is integrated with a printing network. Lulu is a common alternative with a more accessible API for this purpose.

---

## 4. Cover and Spine Formatting

The cover is a separate file from the manuscript and must be formatted precisely.

### 4.1. Cover Page

*   **File Format:** A single, flattened PDF that includes the front cover, back cover, and spine all in one image.
*   **Front Cover:** Should feature the book title and the main character in a vibrant, eye-catching illustration.
*   **Back Cover:** Can include a short blurb about the story, a small picture of a character, and a placeholder for the ISBN barcode (which KDP will add).

### 4.2. Spine Text

*   **Content:** `Book Title` - `Author Name`
*   **Formatting:** The text must be centered on the spine area of the cover PDF.
*   **Calculation:** The width of the spine depends on the page count and paper type. For an ~24-page, 8.5x8.5" book with premium color paper, the spine will be very thin (e.g., ~0.06 inches). KDP provides a cover calculator tool to get the exact dimensions. Text may not be feasible on such a thin spine and could be omitted.
